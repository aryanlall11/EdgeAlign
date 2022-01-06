n_pixels = 3
window = 30
lseqs = 1500

n_actions = 3
rewards = [1, -0.5, -0.5]
"""
Match : 1, Unmatch : -0.5, Insert : -0.5, Deletion : -0.5
"""

maxIndel = 2     # Maximum InDel length
p_snp = 0.1      # Probability of SNP
p_indel = 0.05   # Probability of indel
zif_s = 1.6      # Zipfian distribution parameter