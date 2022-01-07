from Tools.SeqGen import *
from Tools.alignment import *

seqgen = SeqGen()
align = Alignment()

for _ in range(1):
    seq1, seq2, lcslength, new = seqgen.getSequences()
    # print("SEQ1 : ", seq1)
    # print("SEQ2 : ", seq2)
    #print("Length : ", lcslength)
    align.reset(seq1, seq2)
    #align.renderSeq(display=True)

    done = False
    rewards_arr = []

    while(not done):
        a = np.random.randint(0, n_actions)
        next_state, reward, done = align.updateSeq(a)
        rewards_arr.append(reward)
    print("Total action :", len(rewards_arr))
    print("Avg reward :", np.mean(rewards_arr))
        
