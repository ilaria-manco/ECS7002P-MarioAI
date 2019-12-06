#################################################
## LSTM model design
#################################################

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, TimeDistributed, Activation, Dropout
from keras.optimizers import Adam

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

    # TODO: generating data during model training
    def generate(self):

        return


# build LSTM model structure
def build_LSTM(dropout, time_steps, num_features, embedding_size, hidden_size, vocabulary, lr, decay_rate):
    model = Sequential()
    model.add(Dropout(dropout, input_shape=(time_steps, num_features)))
    if embedding_size > 0:
        model.add(TimeDistributed(Dense(embedding_size)))
    model.add(LSTM(hidden_size, return_sequences=True))
    model.add(Dropout(dropout))
    model.add(TimeDistributed(Dense(vocabulary)))
    model.add(Activation('softmax'))

    optimizer = Adam(lr=lr, decay=decay_rate)
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    print(model.summary())
    return model