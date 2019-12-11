# MarioLevel-RNN
generating Mario Levels using RNN. (ECS7002 Assignment 2)

The generated levels are going to be used in [Mario Framework](https://github.com/amidos2006/Mario-AI-Framework) in module ECS7002P Artificial Intelligence in Games, Assignment 2.

## Installation

Model built in this project is using Python 3, based on [Tensorflow](https://www.tensorflow.org/) and [Keras](https://keras.io/).

Before running, please install all the requirements by running:

    pip install -r requirements.txt

## Generate Mario Level

A pre-trained model is provided as `runs/model_best.hdf5`, use the following command to generate Mario Levels, indicating how many levels you want to generate (by default, the command will generate 2 levels):

    python generate_level.py <number_of_levels>

Please find the generated levels in `new_levels` folder.

## Data

Run the following command to divide dataset into training, validation and testing.

    python data_preparation.py

## Training

To train the model, please run:

    python train.py

You can also train other model architectures by running

    python train.py --bi_directional <0/1> --snaking <0/1> --start_from_top <0/1>

please indicate your choice in the command (`yes - 1, no - 0`).