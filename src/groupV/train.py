###########################
## model training
###########################

import argparse
from keras.callbacks import ModelCheckpoint
from configs import *
import utils
from model import *
import warnings
warnings.filterwarnings("ignore")

# parser arguments
parser = argparse.ArgumentParser()
parser.add_argument('--word_rnn', type=bool, default=False, help='train a word rnn which takes stripes as words in model? 0 - No, 1 - Yes')
parser.add_argument('--bi_directional', type=bool, default=False, help='use bi-directional LSTM model? 0 - No, 1 - Yes')
parser.add_argument('--snaking', type=bool, default=False, help='use snaking in data representation? 0 - No, 1 - Yes')
parser.add_argument('--start_from_top', type=bool, default=False, help='start from top during encoding data representation? 0 - No, 1 - Yes')
args = parser.parse_args()


# load training, testing, and validation data
if args.word_rnn:
    train_data = utils.load_data_word(TRAINING)
    valid_data = utils.load_data_word(VALIDATION)
    num_features, vocabulary = utils.get_dict_size()
else:
    train_data = utils.load_data(TRAINING, snaking=args.snaking, start_from_top=args.start_from_top)
    valid_data = utils.load_data(VALIDATION, snaking=args.snaking, start_from_top=args.start_from_top)

# create batch generators
train_data_generator = KerasBatchGenerator(train_data, batch_size, time_steps, num_features, vocabulary, skip_step)
valid_data_generator = KerasBatchGenerator(valid_data, batch_size, time_steps, num_features, vocabulary, skip_step)

# create LSTM model
model = build_LSTM(dropout, time_steps, num_features, embedding_size, hidden_size, vocabulary, lr, decay_rate, bi_directional=args.bi_directional)

# design checkpoint
checkpointer = ModelCheckpoint(filepath="runs\\models\\model_{epoch}.hdf5", verbose=1)
plot_losses = PlotLosses("runs\\plots\\")

# get number of batches for each epoch
steps_per_epoch = 0
for i in range(len(train_data)):
    steps_per_epoch += (train_data[i].shape[0] - time_steps) // skip_step
steps_per_epoch = steps_per_epoch // batch_size
validation_steps = 0
for i in range(len(valid_data)):
    validation_steps += (valid_data[i].shape[0] - time_steps) // skip_step
validation_steps = validation_steps // batch_size

# model training
model.fit_generator(train_data_generator.generate(), steps_per_epoch, num_epochs, validation_data=valid_data_generator.generate(), validation_steps=validation_steps, callbacks=[checkpointer, plot_losses])
