############################
## constant definitions
############################

# dataset
DATASET_PATH = '..\\..\\levels\\'

TRAINING = 'data\\training.txt'
VALIDATION = 'data\\validation.txt'
TESTING = 'data\\testing.txt'

# model configs
batch_size = 128
time_steps = 32
num_features = 12
embedding_size = 0     # 0 for no embedding layer
hidden_size = 12
vocabulary = 12

# model traing configs
skip_step = 3
dropout = 0.4
lr = 0.001
decay_rate = 0.1 ** 6

