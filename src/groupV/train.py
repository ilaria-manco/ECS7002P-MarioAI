###########################
## model training
###########################

from keras.callbacks import ModelCheckpoint
from configs import *
import utils
from model import *
import warnings
warnings.filterwarnings("ignore")

# load training, testing, and validation data
train_data = utils.load_data(TRAINING)
valid_data = utils.load_data(VALIDATION)

# create batch generators
train_data_generator = KerasBatchGenerator(train_data, batch_size, time_steps, num_features, vocabulary, skip_step)
valid_data_generator = KerasBatchGenerator(valid_data, batch_size, time_steps, num_features, vocabulary, skip_step)

# create LSTM model
model = build_LSTM(dropout, time_steps, num_features, embedding_size, hidden_size, vocabulary, lr, decay_rate)

# TODO: design checkpoint

# TODO: get number of batches for each epoch

# TODO: model training