# Install

```
pip install git+https://github.com/alexandreprl/AMAK-Python.git#egg=amak
```

# Quick start

## Headless
```python

from amak import MAS, Agent, Scheduler


class MyAMAS(MAS):
    def __init__(self, environment):
        super().__init__(environment)
        # Code that should be performed after MAS initialization


class MyAgent(Agent):
    def __init__(self, amas):
        super().__init__(amas)
        # Code that should be performed after agent initialization
        self.i = 0

    def on_perceive(self):
        pass

    def on_decide(self):
        pass

    def on_act(self):
        self.i += 1

    def is_ready_to_stop(self):
        return self.i == 100

class MyEnvironment:
    def cycle(self):
        pass

environment = MyEnvironment()
amas = MyAMAS(environment)

MyAgent(amas)

Scheduler(amas, environment).start()
```


## With pygame
```python
from amak import MAS, Agent, AMAKPygame


class MyAMAS(MAS):
    def __init__(self, environment):
        super().__init__(environment)
        # Code that should be performed after MAS initialization


class MyAgent(Agent):
    def __init__(self, amas):
        super().__init__(amas)
        # Code that should be performed after agent initialization
        self.i = 0

    def on_perceive(self):
        pass

    def on_decide(self):
        pass

    def on_act(self):
        self.i += 1

    def is_ready_to_stop(self):
        return self.i == 100


class MyEnvironment:
    def cycle(self):
        pass


environment = MyEnvironment()
amas = MyAMAS(environment)

MyAgent(amas)

if __name__ == '__main__':
    AMAKPygame(amas, environment)
```