import numpy as np
import random

class MRP_BellmanEquation:

    def __init__(self, number_of_state, gamma):
        self.number_of_state = number_of_state
        self.state_value_vector = np.zeros((number_of_state, 1), dtype=float)
        self.gamma = gamma
        self.reward_vector = np.zeros((number_of_state, 1), dtype=float)
        self.probabilistic_transaction_matrix = np.zeros((number_of_state, number_of_state), dtype=float)

    def bellman_equation_initialize_paramters(self):
        self.probabilistic_transaction_matrix = [[random.randrange(0,1) for i in range(self.number_of_state)] for j in range(self.number_of_state)]
        self.state_value_vector = [random.randrange(0,1) for i in range(self.number_of_state)]
        self.reward_vector = [random.randrange(0,1) for i in range(self.number_of_state)]

    def bellman_equation(self):
        self.state_value_vector = np.dot(self.reward_vector, (np.eye(self.number_of_state) - self.gamma*self.probabilistic_transaction_matrix))
        retunr self.state_value_vector

