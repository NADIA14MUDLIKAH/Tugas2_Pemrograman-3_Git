import csv
import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data, dtype=float)

    def __add__(self, other):
        return Matrix(self.data + other.data)

    def __matmul__(self, other):
        return Matrix(self.data @ other.data)

    def transpose(self):
        return Matrix(self.data.T)

    def inverse(self):
        return Matrix(np.linalg.inv(self.data))

    @staticmethod
    def from_csv(file_path):
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            data = [list(map(float, row)) for row in reader if row]
        return Matrix(data)

    def __repr__(self):
        return str(self.data)
