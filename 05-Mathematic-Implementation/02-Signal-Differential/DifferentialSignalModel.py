#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2021"
__status__ = "Created"
__version__ = "2021.04.22"

import numpy as np
import random
from DifferentialSignalLog import Log


class DifferentialSignalModel(Log):
    def __init__(self, input_signal_vector, sensitive_mode=False):
        super().__init__()
        self.number_of_wires = len(input_signal_vector)
        self.signal_vector = input_signal_vector

        if sensitive_mode:
            self.signal_encoder_matrix = np.zeros((self.number_of_wires, self.number_of_wires - 1), dtype=float)
        else:
            self.signal_encoder_matrix = np.zeros((self.number_of_wires, self.number_of_wires), dtype=float)

        for i in range(len(self.signal_encoder_matrix)):
            for j in range(len(self.signal_encoder_matrix[0])):
                if i == j and i != self.number_of_wires - 1:
                    self.signal_encoder_matrix[i][j] = 1
                elif j == self.number_of_wires - 1:
                    self.signal_encoder_matrix[i][j] = 1 / (self.number_of_wires - 1)
                else:
                    self.signal_encoder_matrix[i][j] = -1 / (self.number_of_wires - 1)
        if sensitive_mode:
            self.signal_decoder_matrix = np.dot(np.linalg.inv(np.dot(self.signal_encoder_matrix.transpose(), self.signal_encoder_matrix)), self.signal_encoder_matrix.transpose())
        else:
            self.signal_decoder_matrix = np.linalg.inv(self.signal_encoder_matrix)

    def encode_signal(self):
        self.log("encode_signal", ', '.join(np.dot(self.signal_encoder_matrix, self.signal_vector)))
        return np.dot(self.signal_encoder_matrix, self.signal_vector)

    def decode_signal(self, input_signal_vector):
        if len(input_signal_vector) > self.number_of_wires:
            self.log("decode_signal", ', '.join(np.dot(self.signal_decoder_matrix, input_signal_vector)))
            return np.dot(self.signal_decoder_matrix, input_signal_vector)
        else:
            self.log("decode_signal", "input signal size conflict")
            return None

    @staticmethod
    def initialize_random_signal(number_of_data):
        return_signal_vector = np.zeros((number_of_data, 1), dtype=float)
        for _ in range(number_of_data):
            return_signal_vector[i] = random.randrange(0, 5)
        return return_signal_vector


if __name__ == "__main__":
    model = DifferentialSignalModel([2,3,3,1], sensitive_mode=True)
    print(model.signal_encoder_matrix)
