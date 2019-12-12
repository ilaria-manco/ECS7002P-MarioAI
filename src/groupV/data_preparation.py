#####################################
## divide train/valid/test dataset
#####################################

import itertools
import random
from configs import *
import utils
from input_format.input_format_utils import *

subsets = ["ge", "hopper", "notch", "ore", "original"]

# get all the file pathes and their names in the dataset
all_files = []
for subset in subsets:

    # get discarded levels per subset
    subset_set = set()
    discarded_levels_file = open("data\\discardedLevels-" + subset + ".txt", 'r', encoding='utf-8')
    discarded_level_filenames = discarded_levels_file.readlines()
    for file in discarded_level_filenames:
        subset_set.add("..\\..\\" + file)

    # get level files
    subset_level_files = utils.get_files(DATASET_PATH + "\\" + subset, '.txt')
    for file in subset_level_files:
        if file not in subset_set:
            all_files.append(file)

# seperate the files into training, validation and testing sets
random.shuffle(all_files)
ratio = [6, 2, 2]   # 60% training, 20% validation, 20% testing

training_set_file = open(TRAINING, "w+")
validation_set_file = open(VALIDATION, "w+")
testing_set_file = open(TESTING, "w+")

for i in range(len(all_files)):
    if i % 10 < ratio[0]:
        training_set_file.write(all_files[i] + '\n')
    elif i % 10 < ratio[0] + ratio[1]:
        validation_set_file.write(all_files[i] + '\n')
    else:
        testing_set_file.write(all_files[i] + '\n')

# create word dictionary
word_to_int_dict = dict()
int_to_word_dict = dict()
word_set = set()
for i in range(len(all_files)):
    columns_array = convert_level_to_columns(all_files[i], True)
    for word in columns_array:
        word_set.add(word)
words = sorted(list(word_set))
word_to_int_dict = dict((c, i) for i, c in enumerate(words))
int_to_word_dict = dict((i, c) for i, c in enumerate(words))

print(word_to_int_dict)
print(int_to_word_dict)
np.save('data\\word_to_int_dict.npy', word_to_int_dict)
np.save('data\\int_to_word_dict.npy', int_to_word_dict)
