"""
-----------------------------------------------------------------------
EdgeAlign: DNA Pairwise Sequence Alignment on Edge Devices using DeepRL
-----------------------------------------------------------------------

Author: Aryan Lall (17D070053), EE, IIT Bombay
Guide : Prof. Siddharth Tallur, EE, IIT Bombay
-----------------------------------------------------------------------
"""

"""
For using the 2 pixel or AutoKeras model, change the "input_size"
variable appropriately to 2-pixel dimensions. Following files use this variable - 
1. RL/environment.py
2. Tools/environment.py  [Change the "a" variable here]
3. Tools/model.py
"""

# !pip install gym
# !pip install keras
# !pip install keras-rl2

import numpy as np
from Param.params import *
from RL.agent import EdgeAlignAgent
from RL.environment import EdgeAlignEnv
from Tools.model import Model
from RL.evaluate import EdgeAlignEvaluate
from Tools.SeqGen import *
from tensorflow.keras.optimizers import Adam
from tensorflow import keras

env = EdgeAlignEnv()

states_shape = env.observation_space.shape
actions_shape = env.action_space.n
print(states_shape)
print(actions_shape)

model_obj = Model()
# use "build_autokeras_model()" for using the AutoKeras model architecture
model = model_obj.build_model()    # 3 pixel model
model.summary()

agent_obj = EdgeAlignAgent()
dqn_agent = agent_obj.build_agent(model=model, enable_dueling_network=True)
dqn_agent.compile(Adam(lr = Learning_Rate), metrics = ['mae'])

# Train RL agent
dqn_agent.fit(env, nb_steps = Num_Episodes, visualize=False, verbose=1)

# Further fine-tuning with lower learning rate
# dqn_agent.compile(Adam(lr = 1e-5), metrics = ['mae'])
# dqn_agent.fit(env, nb_steps = Num_Episodes, visualize=False, verbose=1)

dqn_agent.save_weights('MyModel', overwrite=True)

model = dqn_agent.model
model.summary()
# model.save("/content/drive/MyDrive/DDP/EdgeAlignModel")  # Save model (This will be used for TFLite)

"""-------------------------------------------------------------------------"""

# model = keras.models.load_model('/content/drive/MyDrive/DDP/EdgeAlignModel')

# Evaluation
scores = dqn_agent.test(env, nb_episodes=10, visualize=False)
print(np.mean(scores.history['episode_reward']))

# Generate random DNA test sequences
seqgen = SeqGen()
seq1, seq2 = seqgen.genSequences()
seqgen.saveSequences(seq1=seq1, seq2=seq2, filename='sample.txt')

# Run pairwise alignment using RL agent on seq1 & seq2
eval = EdgeAlignEvaluate()
eval.model = model
eval.align(seq1=seq1, seq2=seq2, filename='alignment.txt')