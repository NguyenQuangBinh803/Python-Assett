import numpy as np
import random

class CameraGeometry:
    def __init__(self, number_of_points):
        self.coordinate_reference = np.zeros((3, 1), dtype=float)
        self.coordinate_image = np.zeros((3, 1), dtype=float)
        self.transform_matrix_homography = np.zeros((3, 3), dtype=float)

        self.scaling_factor = 1
        self.camera_intrinsic = np.zeros((3, 3), dtype=float)
        self.transform_matrix = np.zeros((3, 4), dtype=float)

        self.number_of_points = number_of_points


    def initialize_random_points(self):
        for _ in range()

if __name__ == "__main__":
    pass
