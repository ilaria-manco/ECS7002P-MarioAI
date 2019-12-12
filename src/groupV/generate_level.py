#############################
##  level generation
#############################

import numpy as np
import argparse
from keras.models import load_model
from configs import *
from model import *
import utils
from input_format.input_format_utils import *
from input_format.mario_level_model import *

parser = argparse.ArgumentParser()
parser.add_argument('run_name', type=str, default=None, help='please specify the name of this run')
parser.add_argument('--num_levels', type=int, default=2, help='please indicate how many levels you want to generate')
parser.add_argument('--word_rnn', type=bool, default=True, help='train a word rnn which takes stripes as words in model? 0 - No, 1 - Yes')
parser.add_argument('--bi_directional', type=bool, default=True, help='use bi-directional LSTM model? 0 - No, 1 - Yes')
parser.add_argument('--snaking', type=bool, default=True, help='use snaking in data representation? 0 - No, 1 - Yes')
parser.add_argument('--start_from_top', type=bool, default=True, help='start from top during encoding data representation? 0 - No, 1 - Yes')
args = parser.parse_args()

# create folders to save generated levels
utils.create_path("levels\\"+ args.run_name)

# load models and seed for level generation
model = load_model("runs\\" + args.run_name + "\\model_best.hdf5")
if args.word_rnn:
    num_features, vocabulary = utils.get_dict_size()
    time_steps = time_steps_word_rnn
seeds = utils.get_seeds(args.num_levels, time_steps, num_features, vocabulary, args.word_rnn, args.snaking, args.start_from_top) # get a list of seeds

for i in range(args.num_levels):
    if args.word_rnn:
        level_data = np.zeros((width, vocabulary), dtype=bool)
    else:
        level_data = np.zeros((width * height, vocabulary), dtype=bool)

    level_data = utils.generate_level_data(level_data, seeds[i], model, time_steps, num_features, vocabulary, args.word_rnn)

    int_array = []
    for t in range(level_data.shape[0]):
        value = utils.onehot_to_int(level_data[t, :])
        int_array.append(value)

    # decode int_arrays into level and save level
    if(args.word_rnn):
        int_to_word_dict = np.load('data\\int_to_word_dict.npy', allow_pickle=True).item()
        level_word_array = decode_level_array_int_to_words(int_array, int_to_word_dict)
        convert_columns_to_level(level_word_array, "levels\\"+args.run_name+"\\level_{}.txt".format(i), top_down=args.start_from_top)
    else:
        level_string = decode_level_array_int_to_string(int_array, int_to_tiles_mapping)
        convert_string_to_level(level_string, "levels\\"+args.run_name+"\\level_{}.txt".format(i), lvl_height=height, snaking=args.snaking, start_from_top=args.start_from_top)
    
