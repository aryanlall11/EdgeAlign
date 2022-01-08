from gym import Env
from gym.spaces import Discrete, Box

from Tools.SeqGen import *
from Tools.alignment import *

seqgen = SeqGen()
align = Alignment()

class EdgeAlignEnv(Env):
    def __init__(self):
        input_size = [n_pixels*(window+2), n_pixels*4, 3]
        self.action_space = Discrete(n_actions)
        self.observation_space = Box(low=0, high=1, shape=(1, input_size[0], input_size[1], input_size[2]), dtype=np.int)
        self.seq1 = []
        self.seq2 = []  
        self.matches = 0
        self.episode_reward = 0
        self.prev_new = False
        self.start = False
        self.ep_num = 1
        self.state = None
        
    def step(self, action):
        self.state, reward, done = align.updateSeq(action)
        info = {}
        self.matches += (reward>0)
        self.episode_reward += reward
        # Return step information
        return self.state, reward, done, info
    
    def reset(self):
        self.seq1, self.seq2, lcslength, new = seqgen.getSequences()
        align.reset(self.seq1, self.seq2)

        if(self.prev_new):
            print("Ep {}: Total Matches = {}, Total Rewards = {}".format(self.ep_num, self.matches, self.episode_reward))
            self.ep_num += 1

        if self.prev_new or (not new) or (not self.start):
            self.matches = lcslength
            self.episode_reward = lcslength*rewards[0]

        self.prev_new = new
        self.start = True
        
        self.state = align.renderSeq()
        return self.state

    def render(self):
        pass