from rl.agents import DQNAgent
from rl.policy import GreedyQPolicy
from rl.memory import SequentialMemory
from EdgeAlign.Param.params import *

class EdgeAlignAgent():
    def __init__(self):
        self.seqmem_limit = 5000
        self.policy = GreedyQPolicy()
        self.nb_steps_warmup = 5000
        pass

    def build_agent(self, model, enable_double_dqn=False, enable_dueling_network=False, dueling_type='avg'):
        memory = SequentialMemory(limit=self.seqmem_limit, window_length=1)

        dqn = DQNAgent(model=model, memory=memory, policy=self.policy, 
                    nb_actions=n_actions, nb_steps_warmup=self.nb_steps_warmup, target_model_update=1e-3,
                    enable_double_dqn=enable_double_dqn, enable_dueling_network=enable_dueling_network,
                    dueling_type=dueling_type)
        return dqn