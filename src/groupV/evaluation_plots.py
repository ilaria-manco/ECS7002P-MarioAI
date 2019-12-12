import numpy as np
from os import listdir
from matplotlib import pyplot as plt
from matplotlib.mlab import griddata
import seaborn as sns

from level_evaluation import LevelMetrics


PATH_TO_GENERATED_LEVELS = "/Users/Ilaria/mario-assignment/src/groupV/new_levels/"
PATH_TO_EXAMPLE_LEVELS = "/Users/Ilaria/mario-assignment/levels/"


class EvaluationPlots:
    def __init__(self, path_to_levels_to_evaluate, level_names=[]):
        self.level_names = level_names
        self.path_to_levels = path_to_levels_to_evaluate
        self.levels = self.get_levels()
        self.leniency = self.get_leniency_array()
        self.linearity = self.get_linearity_array()

    def get_levels(self):
        """ Get list of all levels to evaluate. If level_names is empty, this contains ALL the levels in the dir """
        levels = []
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
        plt.show()

    def leniency_linearity_contour(self):
        plt.hist2d(self.leniency, self.linearity)
        sns.set_style("white")
        # sns.kdeplot(self.leniency, self.linearity, cmap="Blues", shade=True, bw=.15)
        sns.jointplot(self.leniency, self.linearity, kind="kde")
        plt.show()


q = EvaluationPlots(PATH_TO_EXAMPLE_LEVELS + "patternCount/")
# q.leniency_histogram()
q.leniency_linearity_contour()
