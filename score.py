import os
import pandas as pd

BP = ['A', 'G', 'C', 'T']  # Nucleotides symbol
scores = [1, -3, 5, 2]
#scores = [1, -0.5, 0.5, 0.5]

#data = {'Sample':[], 'Seq1 Length':[], 'Seq2 Length':[], 'Matches':[], 'Gap score':[], 'Total score':[], 'RL Matches':[], 'RL Gap score':[], 'RL Total score':[]}

def get_idx(seq, idx):
	p = 0
	for i in range(len(seq))[::idx]:
		if(seq[i] in BP):
			p = i
			break
	return p

def score(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
	f.close()

	seq1 = lines[1].strip()
	seq2 = lines[3].strip()
	
	# print("Seq1 Length : ", len(seq1))
	# print("Seq2 Length : ", len(seq2))
	# print("---------------------------")

	s1 = get_idx(seq1, 1)
	e1 = get_idx(seq1, -1)
	s2 = get_idx(seq2, 1)
	e2 = get_idx(seq2, -1)

	if(s2>s1):
		s = s2
	else:
		s = s1

	if(e2>e1):
		e = e1
	else:
		e = e2

	isgap1 = False
	isgap2 = False

	match_score = 0
	gap_score1 = 0
	gap_score2 = 0
	total_matches = 0
	mismatch = 0

	for i in range(s, e+1):
		if(seq1[i] == seq2[i] and seq1[i] in BP):
			match_score += scores[0]
			total_matches += 1
			isgap1 = False
			isgap2 = False

		elif(seq1[i] == '-' or seq2[i] == '-'):
			if(seq1[i] == '-'):
				if(not isgap1):
					isgap1 = True
					gap_score1 += scores[2]
				else:
					gap_score1 += scores[3]
			else:
				isgap1 = False

			if(seq2[i] == '-'):
				if(not isgap2):
					isgap2 = True
					gap_score2 += scores[2]
				else:
					gap_score2 += scores[3]
			else:
				isgap2 = False		

		else:
			match_score += scores[1]
			mismatch += 1
			isgap1 = False
			isgap2 = False

	total_score = match_score - (gap_score1 + gap_score2)
	#print(mismatch)
	# print("Total matches : {}".format(total_matches))
	# print("Identity score : {}".format(match_score))
	# print("Gap score : {}".format(gap_score1 + gap_score2))
	# print("Alignment Score: {}".format(total_score))
	# print("\n")
	return total_matches, gap_score1 + gap_score2, total_score

def score_alignment(fasta):
	with open(fasta, 'r') as f:
		lines = f.readlines()
	f.close()

	seq1 = lines[1].strip()
	seq2 = lines[3].strip()
	data['Sample'].append(fasta)
	data['Seq1 Length'].append(len(seq1))
	data['Seq2 Length'].append(len(seq2))

	alnfile = fasta.replace('.fasta', '.aln')
	tm, gs, ts = score(alnfile)
	data['Matches'].append(tm)
	data['Gap score'].append(gs)
	data['Total score'].append(ts)

	tm, gs, ts = score('e' + alnfile)
	data['RL Matches'].append(tm)
	data['RL Gap score'].append(gs)
	data['RL Total score'].append(ts)

# files = os.listdir(os.getcwd())
# for file in files:
# 	if('.fasta' in file):
# 		print(file)
# 		score_alignment(file)

# df = pd.DataFrame(data)   
# df.to_csv('Influenza.csv', index=False, columns=["Sample", "Seq1 Length", "Seq2 Length", 'Matches', 'RL Matches', 'Gap score', 'RL Gap score', 'Total score', 'RL Total score'])
