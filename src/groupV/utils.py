##########################
## helper functions
##########################
import os
from input_format.input_format_utils import *
from input_format.mario_level_model import *
from configs import *

# get a list of all the sub paths under the given folder.
def get_sub_paths(path):
    try:
        sub_paths = [os.path.join(path, o) for o in os.listdir(path) if os.path.isdir(os.path.join(path, o))]
        return sub_paths
    except OSError as e:
        print('Error: Invalid path!')
        return []

# get a list of all the filenames under the given folder with defined suffix.
def get_files(path, suffix):
    try:
        filenames = [os.path.join(path, p) for p in os.listdir(path) if suffix in p]
        return filenames
    except OSError as e:
        print('Error: Invalid path!')
        return []

# load data from dataset files:
def load_data(dataset_filename, snaking=False, start_from_top=False):
    dataset_file = open(dataset_filename, 'r', encoding='utf-8')
    level_filenames = dataset_file.readlines()
    data = []

    for i in range(len(level_filenames)):
        try:
            columns_array = convert_level_to_string(level_filenames[i][:-1], snaking=snaking, start_from_top=start_from_top)
            int_array = encode_level_string_to_array_int(columns_array, tiles_to_int_mapping)
            new_data_from_file = np.zeros((len(int_array), len(all_tiles)), dtype=bool)
            for j in range(len(int_array)):
                new_data_from_file[j, int_array[j]] = 1
            data.append(new_data_from_file)
        except:
            print("cannot convert level file: " + level_filenames[i])

    return data

# create folder if not exist
def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


# load training and validation data for word rnn.
def load_data_word(dataset_filename):
    word_to_int_dict = np.load('data\\word_to_int_dict.npy').item()
    dataset_file = open(dataset_filename, 'r', encoding='utf-8')
    level_filenames = dataset_file.readlines()
    data = []

    for i in range(len(level_filenames)):
        try:
            columns_array = convert_level_to_columns(level_filenames[i][:-1], True)
            new_data_from_file = np.zeros((len(columns_array), len(word_to_int_dict)), dtype=bool)
            for j in range(len(columns_array)):
                new_data_from_file[j, word_to_int_dict[columns_array[j]]] = 1
            data.append(new_data_from_file)
        except:
            print("cannot convert level file: " + level_filenames[i])

    return data


def get_dict_size():
    size = len(np.load('data\\word_to_int_dict.npy').item())
    return size, size