n_pixels = 3   # Each nucleotide is represented using (n_pixels x n_pixels)
window = 50    # Window size used for training
lseqs = 1500   # Length of sequences used for training

n_actions = 3  # Forward, Insert and Delete

"""
Match : 1, Unmatch : -0.6, Gap open : -1, Gap extension : -0.4
"""
rewards = [1, -0.6, -1, -0.4]
#rewards = [1, -0.5, -0.5, -0.5]   # Also try training with these rewards

maxIndel = 2     # Maximum InDel length
p_snp = 0.1      # Probability of SNP
p_indel = 0.05   # Probability of indel
zif_s = 1.6      # Zipfian distribution parameter

BP = ['A', 'G', 'C', 'T']  # Nucleotide symbols

Learning_Rate = 1e-4
Num_Episodes = 60000