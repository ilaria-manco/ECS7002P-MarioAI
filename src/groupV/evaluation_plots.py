import numpy as np
from os import listdir
from glob import glob
from matplotlib import pyplot as plt
import seaborn as sns

from level_evaluation import LevelMetrics


PATH_TO_GENERATED_LEVELS = "/Users/Ilaria/mario-assignment/src/groupV/levels/word-bi-lstm/"
PATH_TO_EXAMPLE_LEVELS = "/Users/Ilaria/mario-assignment/levels/"
PATH_TO_TRAINING_DATA = "/Users/Ilaria/mario-assignment/src/groupV/data/training.txt"


class EvaluationPlots:
    def __init__(self, path_to_levels_to_evaluate, level_names=[], training_data=True):
        self.level_names = level_names
        self.training_data = training_data
        self.path_to_levels = path_to_levels_to_evaluate
        self.levels = self.get_levels()
        self.leniency = self.get_leniency_array()
        self.linearity = self.get_linearity_array()

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

    def get_linearity_array(self):
        linearities = []
        for level in self.levels:
            linearities.append(level.linearity)

        return np.array(linearities)

    def get_density_array(self):
        densities = []
        for level in self.levels:
            densities.append(level.linearity)

        return np.array(densities)

    def leniency_histogram(self):
        plt.hist(self.leniency, histtype="step", bins=int(len(self.leniency)/20))

    def leniency_linearity_contour(self):
        plt.hist2d(self.leniency, self.linearity)
        sns.set_style("white")
        sns.jointplot(self.leniency, self.linearity, kind="kde").set_axis_labels("Leniency $l$", "Linearity $R^{2}$")
        plt.tight_layout()
        plt.savefig("./plots/len_vs_lin", dpi=300)


# q = EvaluationPlots(PATH_TO_EXAMPLE_LEVELS, training_data=True)
# q.leniency_histogram()
# q.leniency_linearity_contour()
