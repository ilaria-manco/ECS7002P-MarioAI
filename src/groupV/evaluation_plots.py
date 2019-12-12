import numpy as np
from os import listdir
from glob import glob
from matplotlib import pyplot as plt
import seaborn as sns

from level_evaluation import LevelMetrics


PATH_TO_GENERATED_LEVELS = "/Users/Ilaria/mario-assignment/src/groupV/levels/word-lstm/"
PATH_TO_EXAMPLE_LEVELS = "/Users/Ilaria/mario-assignment/levels/"
PATH_TO_TRAINING_DATA = "/Users/Ilaria/mario-assignment/src/groupV/data/training.txt"


class EvaluationPlots:
    def __init__(self, path_to_levels_to_evaluate, level_names=[], training_data=True):
        self.level_names = level_names
        self.training_data = training_data
        self.path_to_levels = path_to_levels_to_evaluate
        self.levels = self.get_levels()

    def get_levels(self):
        """ Get list of all levels to evaluate. If level_names is empty, this contains ALL the levels in the dir """
        levels = []
        if self.training_data:
            names = []
            for subdirectory in glob(self.path_to_levels + "/*/"):
                sub = listdir(subdirectory)
                for level in sub:
                    names.append(subdirectory + level)
            for name in names:
                levels.append(LevelMetrics(name))
        else:
            if not self.level_names:
                names = listdir(self.path_to_levels)
            else:
                names = self.level_names
            for name in names:
                levels.append(LevelMetrics(self.path_to_levels + name))
        return levels

    def get_leniency_array(self):
        leniencies = []
        for level in self.levels:
            leniencies.append(level.leniency)

        return np.array(leniencies)

    def get_gaps_array(self):
        gaps = []
        for level in self.levels:
            gaps.append(level.get_gaps_in_the_floow())

        return np.array(gaps)

    def get_linearity_array(self):
        linearities = []
        for level in self.levels:
            linearities.append(level.linearity)

        return np.array(linearities)

    def get_density_array(self):
        densities = []
        for level in self.levels:
            densities.append(level.density)

        return np.array(densities)

    def get_enemy_density_array(self):
        densities = []
        for level in self.levels:
            densities.append(level.get_enemy_density())

        return np.array(densities)

    def density_histogram(self):
        plt.hist(self.get_density_array(), histtype="step", bins=30)
        plt.xlabel("Density")
        plt.savefig("./plots/density", dpi=300)

    def enemy_histogram(self):
        plt.hist(self.get_enemy_density_array(), histtype="step", bins=5)
        plt.xlabel("Enemy density")
        plt.savefig("./plots/enemy_density", dpi=300)

    def gaps_histogram(self):
        plt.hist(self.get_gaps_array(), histtype="step", bins=20)
        plt.xlabel("Number of gaps in the floor")
        plt.savefig("./plots/gaps", dpi=300)

    def leniency_linearity_contour(self):
        leniency = self.get_leniency_array()
        linearity = self.get_linearity_array()
        plt.hist2d(leniency, linearity)
        sns.set_style("white")
        sns.jointplot(leniency, linearity, kind="kde").set_axis_labels("Leniency $l$", "Linearity $R^{2}$")
        plt.tight_layout()
        plt.savefig("./plots/len_vs_lin", dpi=300)


q = EvaluationPlots(PATH_TO_GENERATED_LEVELS, training_data=False)
# q = EvaluationPlots(PATH_TO_EXAMPLE_LEVELS, training_data=True)
# q.density_histogram()
q.leniency_linearity_contour()
