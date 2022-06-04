import os

def align(filename):
	seq1 = []
	seq2 = []
	with open(filename, 'r') as f:
		lines = f.readlines()
	f.close()
	
	i = 1
	while('>ref|' not in lines[i]):
		i = i+1
	i = i+1
	
	while('>' not in lines[i]):
		seq1.append(lines[i].strip())
		i=i+1
	i = i+1

	for l in lines[i: ]:
		seq2.append(l.strip())

	seq1 = "".join(seq1)
	seq2 = "".join(seq2)

	print(filename)
	print(len(seq1.replace('-', '')))
	print(len(seq2.replace('-', '')))
	print("\n")

	s = ">seq1\n" + seq1 + "\n>seq2\n" + seq2

	with open(filename, 'w') as f:
		f.write(s)
	f.close()

files = os.listdir(os.getcwd())

for file in files:
	if('.aln' in file):
		align(file)