# !pip install gym
# !pip install keras
# !pip install keras-rl2

import numpy as np
from EdgeAlign.Param.params import *
from EdgeAlign.RL.agent import EdgeAlignAgent
from EdgeAlign.RL.environment import EdgeAlignEnv
from EdgeAlign.Tools.model import Model
from EdgeAlign.RL.evaluate import EdgeAlignEvaluate
from EdgeAlign.Tools.SeqGen import *
from tensorflow.keras.optimizers import Adam
from tensorflow import keras

env = EdgeAlignEnv()

states_shape = env.observation_space.shape
actions_shape = env.action_space.n
print(states_shape)
print(actions_shape)

model_obj = Model()
model = model_obj.build_model()
model.summary()

agent_obj = EdgeAlignAgent()
dqn_agent = agent_obj.build_agent(model=model, enable_dueling_network=True)
dqn_agent.compile(Adam(lr = Learning_Rate), metrics = ['mae'])
# Train RL agent
dqn_agent.fit(env, nb_steps = Num_Episodes, visualize=False, verbose=1)

model = dqn_agent.model
model.summary()
model.save("/content/drive/MyDrive/DDP/EdgeAlignModel")  # Save model

"""-------------------------------------------------------------------------"""

# model = keras.models.load_model('/content/drive/MyDrive/DDP/EdgeAlignModel')

# Evaluation
scores = dqn_agent.test(env, nb_episodes=10, visualize=False)
print(np.mean(scores.history['episode_reward']))

# Generate random DNA test sequences
seqgen = SeqGen()
seq1, seq2 = seqgen.genSequences()
seqgen.saveSequences(seq1=seq1, seq2=seq2, filename='sample.txt')

eval = EdgeAlignEvaluate()
eval.model = model
eval.align(seq1=seq1, seq2=seq2, filename='alignment.txt')