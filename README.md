# EdgeAlign

DNA Sequence Alignment using Deep Reinforcement Learning on Edge-devices

Author: Aryan Lall, EE, IIT Bombay

Guide : Prof. Siddharth Tallur, EE, IIT Bombay

----
main_train.py - Train the deep RL agent

main_benchmark.py - Obtain the mean error for a given model on the Influenza dataset

Autokeras.py - Perform network architecture search for EdgeAlign model using AutoKeras

model-to-TFLite - Convert Keras model to TFLite format for Microcontrollers

score.py - Obtain the BLAST alignment score for RL agent and compare it with the Influenza dataset

----
Models_final - Folder containing model weights of trained RL agent for 5 different window sizes

Influenza - Folder containing Influeza dataset samples (size: 40)

auto_data - Dataset required for training AutoKeras model (states & action for window 50)
