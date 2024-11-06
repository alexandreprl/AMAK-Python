# Install

```
pip install git+https://github.com/alexandreprl/AMAK-Python.git#egg=amak
```

# Quick start
```python

from amak import MAS, Agent, Scheduler

class MyAMAS(MAS):
    def __init__(self, environment, distance_threshold, fuse_method, distance_method):
        super().__init__(environment)
        # Code that should be performed after MAS initialization

class MyAgent(Agent):
    def __init__(self, amas):
        super().__init__(amas)
        # Code that should be performed after agent initialization

    def on_perceive(self):
        pass

    def on_decide(self):
        pass

    def on_act(self):
        pass

class MyEnvironment:
    def cycle(self):
        pass

def environment = MyEnvironment()
def amas = MyAMAS(environment)

MyAgent(amas)

def scheduler = Scheduler(amas, environment)
scheduler.start()
