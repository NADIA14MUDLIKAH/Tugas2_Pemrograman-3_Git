from matrix_regression.matrix import Matrix
import numpy as np

class LinearRegressionMatrix:
    def __init__(self, X, y):
        self.X = np.c_[np.ones(len(X)), X]  # tambahkan intercept
        self.y = y.reshape(-1, 1)
        self.coef_ = None

    def fit(self):
        X = self.X
        y = self.y
        # Rumus OLS: (X'X)^(-1) X'y
        self.coef_ = np.linalg.inv(X.T @ X) @ X.T @ y
        return self.coef_

    def predict(self, X_new):
        X_new = np.c_[np.ones(len(X_new)), X_new]
        return X_new @ self.coef_

    def summary(self):
        return f"Intercept = {self.coef_[0][0]:.4f}, Slope = {self.coef_[1][0]:.4f}"

