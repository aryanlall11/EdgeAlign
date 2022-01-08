from rl.agents import DQNAgent
from rl.policy import GreedyQPolicy
from rl.memory import SequentialMemory
from Param.params import *

class EdgeAlignAgent():
    def __init__(self):
        self.seqmem_limit = 5000
        self.policy = GreedyQPolicy()
        self.nb_steps_warmup = 5000
        pass

    def build_agent(self, model):
        memory = SequentialMemory(limit=self.seqmem_limit, window_length=1)

        dqn = DQNAgent(model=model, memory=memory, policy=self.policy, 
                    nb_actions=n_actions, nb_steps_warmup=self.nb_steps_warmup, target_model_update=1e-3)
        return dqn