#################################################
## LSTM model design
#################################################

import numpy as np
import matplotlib.pyplot as plt
from shutil import copyfile
from keras.models import Sequential
from keras.layers import Dense, LSTM, TimeDistributed, Activation, Dropout, Bidirectional
from keras.optimizers import Adam
from keras.callbacks import Callback

# batch generator
class KerasBatchGenerator(object):
    def __init__(self, data, batch_size, time_steps, num_features, vocabulary, skip_step):
        self.data = data
        self.current_index = 0
        self.file_index = 0
        self.batch_size = batch_size
        self.time_steps = time_steps
        self.num_features = num_features
        self.vocabulary = vocabulary
        self.skip_step = skip_step

    # generating data during model training
    def generate(self):
        x = np.zeros((self.batch_size, self.time_steps, self.num_features), dtype=np.bool)
        y = np.zeros((self.batch_size, self.time_steps, self.vocabulary), dtype=np.bool)

        while True:
            for i in range(self.batch_size):
                if self.current_index + self.time_steps + 1 >= len(self.data[self.file_index][0]):
                    self.current_index = 0
                    self.file_index = (self.file_index + 1) % len(self.data)

                x[i, :, :] = self.data[self.file_index][self.current_index : self.current_index + self.time_steps, :]
                y[i, :, :] = self.data[self.file_index][self.current_index + 1 : self.current_index + self.time_steps + 1, :]

                self.current_index += self.skip_step

            yield x, y


# plot loss graph and save best model after each epoch
class PlotLosses(Callback):
    def __init__(self, path):
        self.losses = []
        self.val_losses = []
        self.accuracies = []
        self.val_accuracies = []
        self.path = path  # path to save losses and accuracies plots

    def on_epoch_end(self, epoch, logs={}):

        # save best model
        if len(self.val_losses) != 0 and logs.get('val_loss') < min(self.val_losses):
            copyfile("runs\\models\\model_{}.hdf5".format(epoch), "runs\\model_best.hdf5")

        # plot losses and acccuracies
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.accuracies.append(logs.get('acc'))
        self.val_accuracies.append(logs.get('val_acc'))

        plt.figure()
        plt.plot(self.losses, 'r-', label='loss')
        plt.plot(self.val_losses, 'g-', label='val_loss')
        plt.title('loss vs. validation loss')
        plt.legend()
        plt.grid(linestyle='--')
        plt.savefig(self.path + 'loss.svg', format='svg')

        plt.figure()
        plt.plot(self.accuracies, 'r-', label='accuracy')
        plt.plot(self.val_accuracies, 'g-', label='val_accuracies')
        plt.title('accuracy vs. validation accuracy')
        plt.legend()
        plt.grid(linestyle='--')
        plt.savefig(self.path + 'accuracy.svg', format='svg')

        # save losses and accuracies into files during training~
        np.save(self.path + 'logs.losses.npy', self.losses)
        np.save(self.path + 'logs.val_losses.npy', self.val_losses)
        np.save(self.path + 'logs.accuracies.npy', self.accuracies)
        np.save(self.path + 'logs.val_accuracies.npy', self.val_accuracies)



# build LSTM model structure
def build_LSTM(dropout, time_steps, num_features, embedding_size, hidden_size, vocabulary, lr, decay_rate, bi_directional=False):
    model = Sequential()
    model.add(Dropout(dropout, input_shape=(time_steps, num_features)))
    if embedding_size > 0:
        model.add(TimeDistributed(Dense(embedding_size)))
    if bi_directional:
        model.add(Bidirectional(LSTM(hidden_size, return_sequences=True)))
    else:
        model.add(LSTM(hidden_size, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(TimeDistributed(Dense(vocabulary)))
    model.add(Activation('softmax'))

    optimizer = Adam(lr=lr, decay=decay_rate)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    print(model.summary())
    return model