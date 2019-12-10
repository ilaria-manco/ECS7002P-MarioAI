import numpy as np
from scipy import stats


class LevelMetrics:
    def __init__(self, level_name):
        self.path = "/Users/Ilaria/mario-assignment/levels/notchParam/" + level_name
        self.text = self.read_level()
        self.matrix = self.get_level_matrix()
        # self.linearity = self.get_linearity()
        # self.leniency = self.get_leniency()
        # self.density = self.get_density()
        # self.pattern_density = self.get_pattern_density()

    def read_level(self):
        with open(self.path) as level_file:
            level_string = level_file.read().splitlines()

        return level_string

    def get_level_matrix(self):
        lines = []
        for line in self.text:
            characters = []
            for character in line:
                characters.append(character)
            lines.append(characters)

        return np.array(lines).T

    def get_mountain_outlines(self):
        hills_and_blocks = np.where(np.logical_or(self.matrix == "#", self.matrix == "%"))
        first_block_x, first_block_y = hills_and_blocks[0][0], hills_and_blocks[1][0]
        mountains_x = [[first_block_x]]
        mountains_y = [[first_block_y]]
        old_x, old_y = hills_and_blocks[0][0], hills_and_blocks[1][0]
        num_mountains = 0
        current_mountain_x = mountains_x[num_mountains]
        current_mountain_y = mountains_y[num_mountains]
        block = 0
        for new_x, new_y in zip(hills_and_blocks[0], hills_and_blocks[1]):
            if new_x == old_x:
                if new_y < old_y:
                    current_mountain_y[block] = new_y
            elif new_x == old_x + 1:
                current_mountain_x.append(new_x)
                current_mountain_y.append(new_y)
                block += 1
            else:
                block = 0
                num_mountains += 1
                mountains_x.append([new_x])
                mountains_y.append([new_y])
                current_mountain_x = mountains_x[num_mountains]
                current_mountain_y = mountains_y[num_mountains]
            old_x = new_x
            old_y = new_y

        return np.array([mountains_x, mountains_y]).T

    def get_linearity(self):
        mountains = self.get_mountain_outlines()
        sum_r_quare = 0
        num_mountains = int(len(mountains)/2)
        index = 0
        while index < num_mountains:
            m, q, r, p, std = stats.linregress(np.array([mountains[index][0], mountains[index][1]]))
            r_square = r**2
            sum_r_quare += r_square
            index += 1
        avg_r_square = sum_r_quare / len(mountains)

        return avg_r_square

    def get_leniency(self):
        # todo
        return None

    def get_density(self):
        # todo
        return None

    def get_pattern_density(self):
        # todo
        return None


example_level = LevelMetrics("lvl-32.txt")
example_matrix = example_level

print(example_matrix.get_linearity())