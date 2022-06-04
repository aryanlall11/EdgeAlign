# !pip install autokeras

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
import autokeras as ak

window = 50
n_pixels = 2
BP = ['A', 'G', 'C', 'T', 'N']
# N represents no nucleotide (usually when window goes past the sequence)

# Each state in the dataset composes of 2 sequences of size window, expressed using nucleotide symbols
states = np.load('states.npy')
actions = np.load('actions.npy')
print(states.shape)
print(actions.shape)

#------------------------------------------------------

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(states, actions, test_size=0.2, random_state=42)

print(x_train.shape)
print(y_train.shape)

#clf = ak.ImageClassifier(overwrite=True)

input_node = ak.ImageInput()

output_node = ak.ImageBlock(
    block_type="vanilla",     # Vanilla network
)(input_node)

output_node = ak.ClassificationHead()(output_node)

clf = ak.AutoModel(
    inputs=input_node, outputs=output_node, overwrite=True, max_trials=20
)

# Fit the AutoKeras model (NAS)
clf.fit(x_train, y_train, validation_split=0.15, epochs=10)

# Export the final model
model = clf.export_model()
model.summary()

#------------------------------------------------------
# Show details of Model layers

ly = model.layers
for i, layer in enumerate (ly):
    print (i, layer)

for i, layer in enumerate (model.layers):
    print (i, layer)
    if hasattr(layer,'kernel_size'):
        print("Kernel size :", layer.kernel_size)
    if hasattr(layer,'strides'):
        print("Strides : ", layer.strides)
    if hasattr(layer,'rate'):
        print("Dropout :", layer.rate)
    if hasattr(layer,'pool_size'):
        print("Pooling size : ", layer.pool_size)
    if hasattr(layer,'activation'):
        print("Activation : ", layer.activation)
    if hasattr(layer,'padding'):
        print("Pad type : ", layer.padding)
    if hasattr(layer,'embeddings_initializer'):
        print(layer.embeddings_initializer)
    print("\n")