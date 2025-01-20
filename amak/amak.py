from enum import Enum


class Agent:
    def __init__(self, amas):
        self.messages = []
        self.amas = amas
        self.amas.agents_pending_addition.append(self)
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
        self.amas.agents_pending_removal.append(self)

class ExecutionPolicy(Enum):
    ONE_PHASE = 1
    TWO_PHASES = 2


class MAS:
    def __init__(self, environment, execution_policy=ExecutionPolicy.ONE_PHASE):
        self.environment = environment
        self.agents = []
        self.agents_pending_addition = []
        self.agents_pending_removal = []
        self.execution_policy = execution_policy

    def cycle(self):
        self.on_system_cycle_start()
        self.remove_pending_agents()
        self.add_pending_agents()
        if self.execution_policy is ExecutionPolicy.ONE_PHASE:
            for agent in self.agents:
                agent.cycle()
        else:
            for agent in self.agents:
                agent.on_perceive()
            for agent in self.agents:
                agent.on_decide_and_act()
        self.remove_pending_agents()
        self.add_pending_agents()
        self.on_system_cycle_end()

    def are_all_agents_ready_to_stop(self):
        all_agents_are_ready_to_stop = all(agent.is_ready_to_stop() for agent in self.agents)
        return all_agents_are_ready_to_stop

    def is_ready_to_stop(self):
        return self.are_all_agents_ready_to_stop()

    def on_system_cycle_start(self):
        pass

    def add_pending_agents(self):
        for agent in self.agents_pending_addition:
            self.agents.append(agent)
        self.agents_pending_addition = []

    def remove_pending_agents(self):
        for agent in self.agents_pending_removal:
            if agent in self.agents:
                self.agents.remove(agent)
        self.agents_pending_removal = []

    def on_system_cycle_end(self):
        pass


class Scheduler:
    def __init__(self, amas, environment):
        self.amas = amas
        self.environment = environment

    def start(self):
        while not self.amas.is_ready_to_stop():
            self.amas.cycle()
            self.environment.cycle()

