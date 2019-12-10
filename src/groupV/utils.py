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

load_data(TRAINING)

# filename = "..\\..\\levels\\original\\lvl-1.txt"

# columns_array = convert_level_to_string(filename, snaking=False, start_from_top=False)
# print()
# print(columns_array)

# encoded = encode_level_string_to_array_int(columns_array, tiles_to_int_mapping)
# print()
# print(encoded)