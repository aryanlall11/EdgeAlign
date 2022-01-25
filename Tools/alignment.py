import  numpy as np
from PIL import Image
from EdgeAlign.Param.params import *

class Alignment():
    def __init__(self):
        self.seq1 = []
        self.seq2 = []
        self.x = 0
        self.y = 0

    def reset(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.x = 0
        self.y = 0
    
    def renderSeq(self, display = False):
        x = self.x
        y = self.y
        sizeS1 = len(self.seq1)
        sizeS2 = len(self.seq2)

        #a = np.zeros([n_pixels*(window+2),n_pixels*4,4]).astype(int)
        a = np.full((window, 2), 4)

        if x+window > sizeS1:
            idx_arr = np.array(self.seq1[x:sizeS1],dtype=int)
            a[0: (sizeS1-x), 0] = idx_arr
        else:
            idx_arr = np.array(self.seq1[x:x+window],dtype=int)
            a[:, 0] = idx_arr

        if y+window > sizeS2:
            idx_arr = np.array(self.seq2[y:sizeS2],dtype=int)
            a[0: (sizeS2-y), 1] = idx_arr
        else:
            idx_arr = np.array(self.seq2[y:y+window],dtype=int)
            a[:, 1] = idx_arr

        word_index = np.array([(5*k[0] + k[1] + 1) for k in a])
        return np.reshape(word_index, word_index.size)

        # # Conversion to RGB
        # r = (1-a[:,:,0])*(1-a[:,:,3])
        # g = (1-a[:,:,1])*(1-a[:,:,3])
        # b = (1-a[:,:,2])*(1-a[:,:,3])
        # a = np.stack([r,g,b], axis=2)

        # if display:
        #     img = Image.fromarray(np.asarray(a*255, dtype = "uint8"), 'RGB')
        #     img = img.transpose(Image.FLIP_TOP_BOTTOM)
        #     img = img.rotate(270, expand = 1)
        #     img.show(title="Rendered Image Sequence")

        #return a
        #return a.reshape(n_pixels*(window+2), n_pixels*4, 3)
        #return np.reshape(a, a.size)  # Resize to 1-dimensional vector

    def updateSeq(self, action):
        if action == 0:
            if self.seq1[self.x] == self.seq2[self.y]:
                reward = rewards[0]  # Match
            else:
                reward = rewards[1]  # Mis-match
            self.x += 1
            self.y += 1

        elif action == 1:            # Seq2 Insertion
            reward = rewards[2]
            self.y += 1

        elif action == 2:            # Seq2 Deletion
            reward = rewards[2]
            self.x += 1

        if(self.x >= len(self.seq1)) or (self.y >= len(self.seq2)):
            done = True
        else:
            done = False

        if not done:
            self.next_state = self.renderSeq()
        
        return self.next_state, reward, done