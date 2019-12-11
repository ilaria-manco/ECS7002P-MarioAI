import numpy as np
# import mario_level_model


# read level from txt file and convert into string depending on ordering parameters
def convert_level_to_string(level_txt_filename, snaking=False, start_from_top=True):
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


# read level from txt file and convert into string depending on ordering parameters
def convert_level_to_string(level_txt_filename, snaking=False, start_from_top=True):
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


# convert string to level depending on ordering parameters and write to txt file
def convert_string_to_level(level_string, level_txt_filename, lvl_height=16, snaking=False, start_from_top=True):
    # array of rows
    level_rows = ['' for x in range(0, lvl_height, 1)]

    level_size = len(level_string)

    if snaking:
        if start_from_top:
            top_down = True
            # write level with snaking starting from top
            for i in range(0, level_size, 1):
                if top_down:
                    level_rows[i % lvl_height] \
                        = level_rows[i % lvl_height] + level_string[i]
                else:
                    level_rows[lvl_height - (i % lvl_height) - 1] \
                        = level_rows[lvl_height - (i % lvl_height) - 1] + level_string[i]
                # change direction
                if i % lvl_height == lvl_height - 1:
                    top_down = not top_down
        else:
            # write level with snaking starting from bottom
            bottom_up = True
            for i in range(0, level_size, 1):
                if bottom_up:
                    level_rows[lvl_height - (i % lvl_height) - 1] \
                        = level_rows[lvl_height - (i % lvl_height) - 1] + level_string[i]
                else:
                    level_rows[i % lvl_height] \
                        = level_rows[i % lvl_height] + level_string[i]
                # change direction
                if i % lvl_height == lvl_height - 1:
                    bottom_up = not bottom_up
    else:
        if start_from_top:
            # write level without snaking starting from top
            for i in range(0, level_size, 1):
                level_rows[i % lvl_height] \
                    = level_rows[i % lvl_height] + level_string[i]
        else:
            # write level without snaking starting from bottom
            for i in range(0, level_size, 1):
                level_rows[lvl_height - (i % lvl_height) - 1] \
                    = level_rows[lvl_height - (i % lvl_height) - 1] + level_string[i]

    # add new line chars at end of lines
    for j in range(0, len(level_rows) - 1, 1):
        level_rows[j] = level_rows[j] + '\n'

    file_writer = open(level_txt_filename, 'w')
    file_writer.writelines(level_rows)
    file_writer.close()


# read level from txt file and split into columns
def convert_level_to_columns(level_txt_filename, top_down=True):
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


# convert columns to level and write to txt file
def convert_columns_to_level(level_words, level_txt_filename, top_down=True):
    # level size
    lvl_width = len(level_words)
    lvl_height = len(level_words[0])
    print(lvl_width)
    print(lvl_height)

    # array of rows
    level_rows = ['' for x in range(0, lvl_height, 1)]

    for i in range(0, lvl_width, 1):
        for j in range(0, lvl_height, 1):
            if top_down:
                level_rows[j] = level_rows[j] + level_words[i][j]
            else:
                level_rows[j] = level_rows[j] + level_words[i][lvl_height - j - 1]

    # add new line chars at end of lines
    for j in range(0, len(level_rows) - 1, 1):
        level_rows[j] = level_rows[j] + '\n'

    file_writer = open(level_txt_filename, 'w')
    file_writer.writelines(level_rows)
    file_writer.close()


# generate a dictionary to map array of words to integers
def generate_words_to_int_mapping(array_of_words):
    words = sorted(list(set(array_of_words)))
    words_to_int = dict((c, i) for i, c in enumerate(words))

    return words_to_int


# generate a dictionary to map integers to array of words
def generate_int_to_words_mapping(array_of_words):
    words = sorted(list(set(array_of_words)))
    int_to_words = dict((i, c) for i, c in enumerate(words))

    return int_to_words


# convert a string representation of level to int representation using mapping dictionary
def encode_level_string_to_array_int(level_string, string_to_int_dict):
    encoded_array = ([string_to_int_dict[char] for char in level_string])
    return encoded_array


# convert an int representation of level to string representation using mapping dictionary
def decode_level_array_int_to_string(level_array_int, int_to_string_dict):
    decoded_string = ''
    for char in level_array_int:
        decoded_string = decoded_string + int_to_string_dict[char]
    return decoded_string


# convert a words representation of level to int representation using mapping dictionary
def encode_level_words_to_array_int(level_words, words_to_int_dict):
    encoded_array = ([words_to_int_dict[word] for word in level_words])
    return encoded_array


# convert an int representation of level to words representation using mapping dictionary
def decode_level_array_int_to_words(level_array_int, int_to_words_dict):
    decoded_array = ([int_to_words_dict[num] for num in level_array_int])
    return decoded_array


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



# filename = "../../../levels/original/lvl-1.txt"
# raw_text = open(filename, 'r', encoding='utf-8')
# # x = raw_text.read()
# # print(x)
# #
# columns_array = convert_level_to_columns(filename, top_down=False)
# print()
# print(columns_array)
#
# words_to_int_dict = generate_words_to_int_mapping(columns_array)
# # print(words_to_int_dict)
# # print("Dictionary size = ", len(words_to_int_dict))
# int_to_words_dict = generate_int_to_words_mapping(columns_array)
# # print(int_to_words_dict)
# # print("Dictionary size = ", len(int_to_words_dict))
#
# encoded = encode_level_words_to_array_int(columns_array, words_to_int_dict)
# print()
# print(encoded)
# print("Encoded size = ", len(encoded))
#
# decoded = decode_level_array_int_to_words(encoded, int_to_words_dict)
# print()
# print(decoded)
#
# convert_columns_to_level(decoded, 'output.txt', top_down=False)

# columns_from_top = convert_level_to_string(filename, snaking=False, start_from_top=True)
# columns_from_bottom = convert_level_to_string(filename, snaking=False, start_from_top=False)
# snaking_from_top = convert_level_to_string(filename, snaking=True, start_from_top=True)
# snaking_from_bottom = convert_level_to_string(filename, snaking=True, start_from_top=False)
#
# print(open(filename, 'r', encoding='utf-8').read())
# print()
# print(snaking_from_bottom)
# print()
# print(columns_from_bottom)
# print()
# print(snaking_from_top)
# print()
# print(snaking_from_bottom)
#
# encoded = encode_level_string_to_array_int(snaking_from_bottom, mario_level_model.tiles_to_int_mapping)
# print()
# print(encoded)
#
# decoded = decode_level_array_int_to_string(encoded, mario_level_model.int_to_tiles_mapping)
# print()
# print(decoded)
#
# convert_string_to_level(decoded, 'output.txt', lvl_height=16, snaking=True, start_from_top=False)
#
# sequences = generate_in_out_sequences(encoded, 30)
# dataX = sequences[0]
# dataY = sequences[1]
# print(dataX[0])
# print(dataY[0])