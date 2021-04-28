from AbstractRegression import AbstractRegression
import numpy as np


class BayesianRegression(AbstractRegression):

    def __init__(self, number_of_parameter):
        super(BayesianRegression, self).__init__(number_of_parameter)
        self.sigma = 0.05

    def function_evaluate(self, data_reference, data_regression):
        return data_reference - np.random.normal(data_regression, self.sigma, 1000)