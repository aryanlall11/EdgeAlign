n_pixels = 3
window = 80
lseqs = 1500

n_actions = 3
"""
Match : 0.5, Unmatch : -0.5, Insert : -1, Deletion : -1
"""
rewards = [1, -0.5, -0.5]

maxIndel = 2     # Maximum InDel length
p_snp = 0.1      # Probability of SNP
p_indel = 0.05   # Probability of indel
zif_s = 1.6      # Zipfian distribution parameter

BP = ['A', 'G', 'C', 'T']  # Nucleotides symbol4

Learning_Rate = 1e-4
Num_Episodes = 40000