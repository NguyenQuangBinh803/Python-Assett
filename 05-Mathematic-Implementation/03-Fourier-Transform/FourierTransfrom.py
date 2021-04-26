import random
import math
import numpy as np
from GraphEngine import GraphicEngine


class FourierTransform:
    def __init__(self, input_signal_vector):
        self.number_of_data = len(input_signal_vector)
        self.number_of_transform = int(self.number_of_data / 2)

        self.input_signal_vector = input_signal_vector

        self.component_real = np.zeros((self.number_of_transform, 1), dtype=float)
        self.component_imaginary = np.zeros((self.number_of_transform, 1), dtype=float)

        self.component_phases = np.zeros((self.number_of_transform, 1), dtype=float)
        self.component_magnitude = np.zeros((self.number_of_transform, 1), dtype=float)

        self.synthesis_signal = np.zeros((self.number_of_data, 1), dtype=float)

        self.graph_engine = GraphicEngine()

    def fourier_transformation(self):
        for k in range(self.number_of_transform):
            self.component_real[k] = sum([self.input_signal_vector[i] * math.cos(2 * math.pi * k * i / self.number_of_data) for i in range(self.number_of_data)])
            self.component_imaginary[k] = sum([-self.input_signal_vector[i] * math.sin(2 * math.pi * k * i / self.number_of_data) for i in range(self.number_of_data)])

    def fourier_calculate_phase_and_mag(self):
        # self.component_phases = math.atan(self.component_imaginary/self.component_real)
        self.component_magnitude = [math.sqrt(self.component_real[i] ** 2 + self.component_imaginary[i] ** 2) for i in range(self.number_of_transform)]

    def fourier_synthesis(self):
        for i in range(self.number_of_data):
            self.synthesis_signal[i] = sum(
                [self.component_real[k] / self.number_of_data * math.cos(2 * math.pi * k * i / self.number_of_data) - self.component_imaginary[k] / self.number_of_data * math.sin(
                    2 * math.pi * k * i / self.number_of_data) for k in
                 range(self.number_of_transform)])

    def plot_signal(self):
        self.graph_engine.plot_signal([self.input_signal_vector, self.component_real, self.component_imaginary, self.synthesisize_signal], [-1, 1])


if __name__ == "__main__":
    input_vector_signal = np.zeros((100, 1), dtype=float)
    for i in range(100):
        input_vector_signal[i] = random.randrange(-1, 1)

    fourier_transform = FourierTransform(input_vector_signal)
    fourier_transform.fourier_transformation()
    fourier_transform.fourier_calculate_phase_and_mag()
    fourier_transform.fourier_synthesis()
    fourier_transform.plot_signal()
