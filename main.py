from Tools.SeqGen import *

seqgen = SeqGen()

for _ in range(6):
    seq1, seq2, lcslength, new = seqgen.getSequences()
    # print("SEQ1 : ", seq1)
    # print("SEQ2 : ", seq2)
    #print("Length : ", lcslength)
    print("New : ", new)