# EdgeAlign

DNA Pairwise Sequence Alignment using Deep Reinforcement Learning on Edge-devices

Author: Aryan Lall, EE, IIT Bombay

Guide : Prof. Siddharth Tallur, EE, IIT Bombay

Refer to https://github.com/aryanlall11/EdgeAlign_Hardware.git for Hardware implementation

----
main_train.py - Train the deep RL agent

main_benchmark.py - Obtain the mean error for a given model on the Influenza dataset

Autokeras.py - Perform network architecture search for EdgeAlign model using AutoKeras

model-to-TFLite.py - Convert Keras model to TFLite format for Microcontrollers

score.py - Obtain the BLAST alignment score for RL agent and compare it with the Influenza dataset

----
Models_final - Folder containing model weights of trained RL agents for 5 different window sizes

Influenza - Folder containing Influeza dataset samples (size: 40)

auto_data - Dataset required for training AutoKeras model (states & action for window 50)

# How to cite EdgeAlign?

If you are using EdgeAlign in your research, please cite the following paper:

Aryan Lall and ‪Siddharth Tallur, “Deep reinforcement learning-based pairwise DNA sequence alignment method compatible with embedded edge devices,” Scientific Reports, vol. 13, no. 1, p. 2773, 2023, doi: 10.1038/s41598-023-29277-6.

```
@article{10.1038/s41598-023-29277-6, 
year = {2023}, 
title = {{Deep reinforcement learning-based pairwise DNA sequence alignment method compatible with embedded edge devices}}, 
author = {Lall, Aryan and Tallur, Siddharth}, 
journal = {Scientific Reports}, 
doi = {10.1038/s41598-023-29277-6}, 
abstract = {{Sequence alignment is an essential component of bioinformatics, for identifying regions of similarity that may indicate functional, structural, or evolutionary relationships between the sequences. Genome-based diagnostics relying on DNA sequencing have benefited hugely from the boom in computing power in recent decades, particularly due to cloud-computing and the rise of graphics processing units (GPUs) and other advanced computing platforms for running advanced algorithms. Translating the success of such breakthroughs in diagnostics to affordable solutions for low-cost healthcare requires development of algorithms that can operate on the edge instead of in the cloud, using low-cost and low-power electronic systems such as microcontrollers and field programmable gate arrays (FPGAs). In this work, we present EdgeAlign, a deep reinforcement learning based method for performing pairwise DNA sequence alignment on stand-alone edge devices. EdgeAlign uses deep reinforcement learning to train a deep Q-network (DQN) agent for performing sequence alignment on fixed length sub-sequences, using a sliding window that is scanned over the length of the entire sequence. The hardware resource-consumption for implementing this scheme is thus independent of the lengths of the sequences to be aligned, and is further optimized using a novel AutoML based method for neural network model size reduction. Unlike other algorithms for sequence alignment reported in literature, the model demonstrated in this work is highly compact and deployed on two edge devices (NVIDIA Jetson Nano Developer Kit and Digilent Arty A7-100T, containing Xilinx XC7A35T Artix-7 FPGA) for demonstration of alignment for sequences from the publicly available Influenza sequences at the National Center for Biotechnology Information (NCBI) Virus Data Hub.}}, 
pages = {2773}, 
number = {1}, 
volume = {13}
}
```
