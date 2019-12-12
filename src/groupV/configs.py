############################
## constant definitions
############################

from input_format.mario_level_model import all_tiles

# dataset
DATASET_PATH = '..\\..\\levels\\'
TRAINING = 'data\\training.txt'
VALIDATION = 'data\\validation.txt'
TESTING = 'data\\testing.txt'

# model configs
batch_size = 128
time_steps = 32
time_steps_word_rnn = 8
num_features = len(all_tiles)
embedding_size = 0     # 0 for no embedding layer
hidden_size = 128
vocabulary = len(all_tiles)

# model traing configs
skip_step = 3
dropout = 0.4
lr = 0.001
decay_rate = 0.1 ** 6
num_epochs = 200

# level generation - dimensions
height = 16
width = 150