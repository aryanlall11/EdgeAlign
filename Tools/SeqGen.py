import numpy as np
import random
from difflib import SequenceMatcher
from EdgeAlign.Param.params import *

class SeqGen():
    
    def __init__(self):
        self.seqgroup = []
        self.grpidx = 0
        self.seq1 = []
        self.seq2 = []
        self.seq1_W = []
        self.seq2_W = []
        pass

    def zipfian(self,s,N):
        temp0 = np.array(range(1,N+1))
        temp0 = np.sum(1/temp0**s)
        temp = random.random() * temp0
        for i in range(N):
            temp2 = 1 / ((i + 1) ** s)
            if temp < temp2:
                return i+1
            else:
                temp = temp - temp2
        return 0

    def genSequences(self):
        seq1 = np.random.randint(4, size=lseqs)

        # SNP Mutation (JC69)
        seq2 = np.mod(seq1 + (np.random.rand(lseqs)  < p_snp)*np.random.randint(4, size=lseqs),4)
        count1 = 0
        count2 = 0
        for kk in range(lseqs):
            if np.random.rand() < p_indel:
                # Indel generation (Zipfian distribution)
                indel = self.zipfian(zif_s, maxIndel)

                ranval = np.random.rand()
                if ranval < 1/2:
                    temp1 = seq1[0:kk+count1]
                    temp4 = seq1[kk+count1:]
                    seq1 = np.append(np.append(temp1,np.random.randint(4, size=indel)),temp4)
                    count1 = count1 + indel
                else:
                    temp2 = seq2[0:kk+count2]
                    temp5 = seq2[kk+count2:]
                    seq2 = np.append(np.append(temp2,np.random.randint(4, size=indel)),temp5)
                    count2 = count2 + indel

        if len(seq1) >= lseqs:
            seq1 = seq1[0:lseqs]
        else:
            tempseq = np.random.randint(4, size=lseqs-len(seq1))
            seq1 = np.append(seq1, tempseq)

        if len(seq2) >= lseqs:
            seq2 = seq2[0:lseqs]
        else:
            tempseq = np.random.randint(4, size=lseqs-len(seq2))
            seq2 = np.append(seq2, tempseq)

        self.seq1 = seq1
        self.seq2 = seq2

        return seq1, seq2

    def lcs(self, seq1, seq2):
        i, j, k = SequenceMatcher(autojunk=False, a=seq1, b=seq2).find_longest_match(0, len(seq1), 0, len(seq2))
        return i,j,k

    def getSequences(self, display=False):        
        while len(self.seqgroup) == 0:
            # Generate sequences from JC69 (SNP) and Zifian model (InDel)
            self.seq1, self.seq2 = self.genSequences()
            # Longest common substring
            s1, s2, length = self.lcs(self.seq1, self.seq2)
            self.lcslength = length
            
            # Reverse sequences
            if(s1 > 0 and s2 > 0):
                # seq1_R = np.append(self.seq1[s1 - 1::-1], [0])
                # seq2_R = np.append(self.seq2[s2 - 1::-1], [0])
                seq1_R = self.seq1[s1 - 1::-1]
                seq2_R = self.seq2[s2 - 1::-1]
                self.seqgroup.append([seq1_R, seq2_R])
            # Forward sequences
            if(s1 + length < len(self.seq1)) and (s2 + length < len(self.seq2)):
                # seq1_F = np.append(self.seq1[s1 + length: ], [0])
                # seq2_F = np.append(self.seq2[s2 + length: ], [0])
                seq1_F = self.seq1[s1 + length: ]
                seq2_F = self.seq2[s2 + length: ]
                self.seqgroup.append([seq1_F, seq2_F])

        # Final working sequence 1
        self.seq1_W = self.seqgroup[self.grpidx][0]
        # Final working sequence 2
        self.seq2_W = self.seqgroup[self.grpidx][1]
        self.grpidx += 1

        gennew = False
        if self.grpidx == len(self.seqgroup):
            gennew = True
            self.seqgroup = []
            self.grpidx = 0

        if display:
            self.printSequences()

        # Return : Working sequences, Longest common length, next should be new?
        return self.seq1_W, self.seq2_W, self.lcslength, gennew
    
    def printSequences(self):
        if(len(self.seq1_W) == 0 or len(self.seq2_W) == 0):
            print("Please first generate the sequences!")
        else:
            seq1 = []
            seq2 = []
            for i in range(len(self.seq1_W)):
                seq1.append(BP[self.seq1_W[i]])
            for i in range(len(self.seq2_W)):
                seq2.append(BP[self.seq2_W[i]])
            seq1 = "".join(seq1)
            seq2 = "".join(seq2)

            print("SEQ1 : " +  seq1)
            print("SEQ2 : " + seq2)

    def saveSequences(self, filename='sample.txt', seq1 = [], seq2 = []):
        if(len(seq1) == 0 or len(seq2) == 0):
            seq1 = self.seq1
            seq2 = self.seq2
        if(len(seq1) == 0 or len(seq2) == 0):
            print("Please first generate the sequences or pass them!")
        else:
            seq1_s = []
            seq2_s = []
            with open(filename, 'w') as f:
                for i in range(len(seq1)):
                    seq1_s.append(BP[seq1[i]])
                for i in range(len(seq2)):
                    seq2_s.append(BP[seq2[i]])
                seq1_s = "".join(seq1_s)
                seq2_s = "".join(seq2_s)
                f.write('>test1\n' + seq1_s + '\n>test2\n' + seq2_s)
