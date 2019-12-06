##########################
## helper functions
##########################
import os

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

# TODO: load data from dataset files:
def load_data(filename):

	return