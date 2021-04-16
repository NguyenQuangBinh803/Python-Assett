import numpy as np
import random


class CameraGeometry:
    def __init__(self, number_of_points):
        self.coordinate_reference = []
        self.coordinate_image = []
        self.coordinate_image_calculation = []
        self.coordinate_image_errors = []

        self.number_of_points = number_of_points
        self.transform_matrix_homography = np.zeros((3, 3), dtype=float)

        self.scaling_factor = 1
        self.camera_intrinsic = np.zeros((3, 3), dtype=float)
        self.transform_matrix = np.zeros((3, 4), dtype=float)

        self.number_of_points = number_of_points

    def initialize_random_points(self):

        for _ in range(self.number_of_points):
            self.coordinate_reference.append([random.randrange(0, 500), [random.randrange(0, 500), [random.randrange(0, 500)])
            self.coordinate_image.append([random.randrange(0, 500), [random.randrange(0, 500), [random.randrange(0, 500)])

    def forward_calculation(self):
        for i in range(self.number_of_points):
            self.coordinate_image_calculation = np.dot(np.dot(self.coordinate_reference, self.camera_intrinsic), self.transform_matrix)

    def backpropagation(self):
        self.coordinate_image_errors = [y - yr for y, yr in zip(self.coordinate_image_calculation, self.coordinate_image)]
        camera_intrinsic_matrix_errors = np.dot(self.coordinate_image_errors, self.transform_matrix)
        coordinate_reference_errors = np.dot(camera_intrinsic_matrix_errors, self.coordinate_reference)

        update_weights = np.dot


if __name__ == "__main__":
    pass
