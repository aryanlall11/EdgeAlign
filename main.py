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
    a = align.renderSeq(displayImage=True)
