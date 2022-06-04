import numpy as np
from Param.params import *
from RL.agent import EdgeAlignAgent
from RL.environment import EdgeAlignEnv
from Tools.model import Model
from RL.evaluate import EdgeAlignEvaluate
from Tools.SeqGen import *
from tensorflow.keras.optimizers import Adam
from tensorflow import keras
from score import *

env = EdgeAlignEnv()

states_shape = env.observation_space.shape
actions_shape = env.action_space.n
print(states_shape)
print(actions_shape)

model_obj = Model()
model = model_obj.build_model()
#model.summary()

agent_obj = EdgeAlignAgent()
dqn_agent = agent_obj.build_agent(model=model, enable_dueling_network=True, dueling_type='avg')
dqn_agent.compile(Adam(lr = Learning_Rate), metrics = ['mae'])
dqn_agent.load_weights('Models_final/EdgeAlign_wb50')     # Load the model with window size 50 (change accordingly)

model = dqn_agent.model
model.summary()

#-----------------------------------------------------------

eval = EdgeAlignEvaluate()
eval.model = model
diff = 0
num = 0
values = []

def align(seq1, seq2):
	seq1_s, seq2_s, _ = eval.align(seq1=seq1, seq2=seq2, filename='alignment.txt')
	s = ">seq1\n" + seq1_s.strip() + "\n>seq2\n" + seq2_s.strip()
	with open('temp.txt', 'w') as f:
		f.write(s)
	f.close()
	tm, gs, ts = score('temp.txt')
	return tm, gs, ts

def compare(fasta):
    alnfile = fasta.replace('.fasta', '.aln')
    tm_o, gs_o, ts_o = score(alnfile)
    with open(fasta, 'r') as f:
        lines = f.readlines()
        seq1 = lines[1].strip()
        seq2 = lines[3].strip()
        tm, gs, ts = align(seq1, seq2)
    f.close()
    global diff
    global values
    if(ts<ts_o):
        it_val = (ts_o-ts)/abs(ts_o)
        diff = diff + it_val
        values.append(it_val)
    else:
        values.append(0)

files = os.listdir(os.getcwd()+'/Influenza')
diff = 0
num = 0
values = []
for file in files:
	if('.fasta' in file):
		num += 1
		print(file)
		compare('Influenza/' + file)
print('---------------------------\n')
print("Mean Error: ", diff/num)

values = np.array(values)
print("Variance: ", np.var(values))