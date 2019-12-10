import numpy as np
import mario_level_model


# read level from txt file and convert into string depending on ordering parameters
def convert_level_to_string(level_txt_filename, snaking = False, start_from_top = True):
    raw_text = open(level_txt_filename, 'r', encoding='utf-8')
    # array of rows
    level_rows = raw_text.readlines()

    # level size
    lvl_width = len(level_rows[0]) - 1
    lvl_height = len(level_rows)

    # remove new line chars at end of lines
    for i in range(0, len(level_rows) - 1, 1):
        level_rows[i] = level_rows[i][0:lvl_width]

    # convert to np array
    level_rows_np = np.array(level_rows)

    level_string = ''

    if snaking:
        if start_from_top:
            top_down = True
            # scan level with snaking starting from top
            for i in range(0, lvl_width, 1):
                for j in range(0, lvl_height, 1):
                    if top_down:
                        level_string = level_string + level_rows_np[j][i]
                    else:
                        level_string = level_string + level_rows_np[lvl_height - j - 1][i]
                # change direction
                top_down = not top_down
        else:
            # scan level with snaking starting from bottom
            bottom_up = True
            for i in range(0, lvl_width, 1):
                for j in range(0, lvl_height, 1):
                    if bottom_up:
                        level_string = level_string + level_rows_np[lvl_height - j - 1][i]
                    else:
                        level_string = level_string + level_rows_np[j][i]
                # change direction
                bottom_up = not bottom_up
    else:
        if start_from_top:
            # scan level without snaking starting from top
            for i in range(0, lvl_width, 1):
                for j in range(0, lvl_height, 1):
                    level_string = level_string + level_rows_np[j][i]
        else:
            # scan level without snaking starting from bottom
            for i in range(0, lvl_width, 1):
                for j in range(0, lvl_height, 1):
                    level_string = level_string + level_rows_np[lvl_height - j - 1][i]

    return level_string


# read level from txt file and split into columns
def convert_level_to_columns(level_txt_filename, top_down = True):
    raw_text = open(level_txt_filename, 'r', encoding='utf-8')
    # array of rows
    level_rows = raw_text.readlines()

    # level size
    lvl_width = len(level_rows[0]) - 1
    lvl_height = len(level_rows)

    # remove new line chars at end of lines
    for i in range(0, len(level_rows) - 1, 1):
        level_rows[i] = level_rows[i][0:lvl_width]

    # convert to np array
    level_rows_np = np.array(level_rows)

    level_columns = []

    for i in range(0, lvl_width, 1):
        level_columns.append('')
        for j in range(0, lvl_height, 1):
            if top_down:
                level_columns[i] = level_columns[i] + level_rows_np[j][i]
            else:
                level_columns[i] = level_columns[i] + level_rows_np[lvl_height - j - 1][i]

    return level_columns


# generate a dictionary to map array of words to integers
def generate_words_to_int_mapping(array_of_words):
    words = sorted(list(set(array_of_words)))
    words_to_int = dict((c, i) for i, c in enumerate(words))

    return words_to_int


# convert a string representation of level using mapping dictionary
def encode_level_string_to_array_int(level_string, string_to_int_dict):
    encoded_array = ([string_to_int_dict[char] for char in level_string])
    return encoded_array


# convert a words representation of level using mapping dictionary
def encode_level_words_to_array_int(level_words, words_to_int_dict):
    encoded_array = ([words_to_int_dict[word] for word in level_words])
    return encoded_array


# generate the input and output sequences to train the LSTM network
def generate_in_out_sequences(encoded_level_string, in_sequence_length):
    tot_length = len(encoded)
    dataX = []
    dataY = []
    for i in range(0, tot_length - in_sequence_length, 1):
        seq_in = encoded_level_string[i:i + in_sequence_length]
        seq_out = encoded_level_string[i + in_sequence_length]
        dataX.append(seq_in)
        dataY.append(seq_out)

    return [dataX, dataY]


#
# filename = "levels/original/lvl-1.txt"
# raw_text = open(filename, 'r', encoding='utf-8')
# x = raw_text.read()
# print(x)
#
# columns_array = convert_level_to_columns(filename, True)
# print()
# print(columns_array)
#
# words_to_int = generate_words_to_int_mapping(columns_array)
# print(words_to_int)
# print("Dictionary size = ", len(words_to_int))
#
# encoded = encode_level_words_to_array_int(columns_array, words_to_int)
# print()
# print(encoded)
# print("Encoded size = ", len(encoded))

# columns_from_top = convert_level_to_string(filename, snaking=False, start_from_top=True)
# columns_from_bottom = convert_level_to_string(filename, snaking=False, start_from_top=False)
# snaking_from_top = convert_level_to_string(filename, snaking=True, start_from_top=True)
# snaking_from_bottom = convert_level_to_string(filename, snaking=True, start_from_top=False)
#
# print(open(filename, 'r', encoding='utf-8').read())
# print()
# print(columns_from_top)
# print()
# print(columns_from_bottom)
# print()
# print(snaking_from_top)
# print()
# print(snaking_from_bottom)
#
# encoded = encode_level_string_to_array_int(columns_from_top, mario_level_model.tiles_to_int_mapping)
# print()
# print(encoded)
#
# sequences = generate_in_out_sequences(encoded, 30)
# dataX = sequences[0]
# dataY = sequences[1]
# print(dataX[0])
# print(dataY[0])