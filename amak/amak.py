class Agent:
    def __init__(self, amas):
        self.messages = []
        self.amas = amas
        self.amas.agents.append(self)
        self.state = 'alive'

    def cycle(self):
        self.on_perceive()
        self.on_decide_and_act()

    def on_perceive(self):
        pass

    def on_decide(self):
        pass

    def on_act(self):
        pass

    def on_decide_and_act(self):
        self.on_decide()
        self.on_act()

    def is_ready_to_stop(self):
        return False

    def tell(self, other, message):
        other.receive(self, message)

    def receive(self, sender, message):
        self.messages.append((sender, message))

    def read_message(self):
        if self.messages:
            return self.messages.pop(0)
        else:
            return None

    def destroy(self):
        self.state = 'destroyed'
        if self in self.amas.agents:
            self.amas.agents.remove(self)


class MAS:
    def __init__(self, environment):
        self.environment = environment
        self.agents = []

    def cycle(self):
        for agent in self.agents:
            agent.cycle()

    def are_all_agents_ready_to_stop(self):
        all_agents_are_ready_to_stop = all(agent.is_ready_to_stop() for agent in self.agents)
        return all_agents_are_ready_to_stop

    def is_ready_to_stop(self):
        return self.are_all_agents_ready_to_stop()


class Scheduler:
    def __init__(self, amas, environment):
        self.amas = amas
        self.environment = environment

    def start(self):
        while not self.amas.is_ready_to_stop():
            self.amas.cycle()
            self.environment.cycle()

