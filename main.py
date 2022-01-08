# !pip install gym
# !pip install keras
# !pip install keras-rl2

import numpy as np
from Param.params import *
from RL.agent import EdgeAlignAgent
from RL.environment import EdgeAlignEnv
from Tools.model import Model
from tensorflow.keras.optimizers import Adam

env = EdgeAlignEnv()

states_shape = env.observation_space.shape
actions_shape = env.action_space.n
print(states_shape)
print(actions_shape)

model_obj = Model()
model = model_obj.build_model()
model.summary()

agent_obj = EdgeAlignAgent()
dqn_agent = agent_obj.build_agent(model=model)
dqn_agent.compile(Adam(lr = Learning_Rate), metrics = ['mae'])
dqn_agent.fit(env, nb_steps = Num_Episodes, visualize=False, verbose=1)

# Evaluation
scores = dqn_agent.test(env, nb_episodes=20, visualize=False)
print(np.mean(scores.history['episode_reward']))

# seqgen = SeqGen()
# align = Alignment()
# model_obj = Model()

# for _ in range(1):
#     seq1, seq2, lcslength, new = seqgen.getSequences()
#     # print("SEQ1 : ", seq1)
#     # print("SEQ2 : ", seq2)
#     #print("Length : ", lcslength)
#     align.reset(seq1, seq2)
#     #align.renderSeq(display=False)

#     done = False
#     rewards_arr = []

#     while(not done):
#         a = np.random.randint(0, n_actions)
#         next_state, reward, done = align.updateSeq(a)
#         rewards_arr.append(reward)
#     print("Total action :", len(rewards_arr))
#     print("Avg reward :", np.mean(rewards_arr))

# model = model_obj.build_model()
# model.summary()

# #print(model.predict(k))
