import numpy as np
import math
import random
from GraphEngine import GraphEngine


class AbstractRegression:
    def __init__(self, number_of_parameter):
        self.regression_function_parameters = np.zeros((number_of_parameter, 1), dtype=float)
        self.acceptable_range = 0.3
        self.learning_rate = 0.1

    def function_regression(self, input_vector):
        output_vector = np.zeros((1, len(input_vector)), dtype=float)
        for index, x in enumerate(input_vector):
            output_vector[index] = sum([math.pow(x, j) * b for j, b in enumerate(self.regression_function_parameters)])
        return output_vector

    def function_evaluate(self, data_reference, data_regression):
        return data_reference - data_regression

    def algorithm_backpropagation(self, input_vector, data_reference):
        data_regression = self.function_regression(input_vector)
        regression_errors = self.function_evaluate(data_reference, data_regression)

        while sum(regression_errors) > self.acceptable_range:
            for error in regression_errors:
                delta_input = np.dot(self.regression_function_parameters, error)
                delta_regression_parameters = np.dot(delta_input, self.regression_function_parameters)
                self.regression_function_parameters = self.regression_function_parameters + self.learning_rate * delta_regression_parameters
            data_regression = self.function_regression(input_vector)
            regression_errors = self.function_evaluate(data_reference, data_regression)


if __name__ == "__main__":
    reference_input = np.zeros((100, 1), dtype=float)
    reference_output = np.zeros((100, 1), dtype=float)

    for i in range(100):
        reference_input[i] = random.randrange(0, 100)
        reference_output[i] = random.randrange(0, 100)

    graph = GraphEngine()
    graph.plot_data(reference_input, reference_output)
    regression_engine = AbstractRegression(4)
