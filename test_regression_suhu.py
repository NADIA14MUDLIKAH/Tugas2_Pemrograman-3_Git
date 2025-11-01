import numpy as np
from matrix_regression.matrix import Matrix

# === 1. Baca data dari CSV ===
m = Matrix.from_csv("data/suhu.csv")

# === 2. Pisahkan X (fitur) dan y (target) ===
# Misal: kolom 1–9 sebagai fitur, kolom ke-10 sebagai target
X = np.array([row[:-1] for row in m.data])
y = np.array([row[-1] for row in m.data]).reshape(-1, 1)

# === 3. Tambahkan kolom 1 untuk intercept ===
X_b = np.hstack([np.ones((X.shape[0], 1)), X])  # menambah kolom 1 di awal

# === 4. Rumus regresi linier (Normal Equation): β = (XᵀX)⁻¹Xᵀy ===
beta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

print("=== Koefisien Regresi (β) ===")
print(beta)

# === 5. Uji prediksi dengan data X pertama ===
y_pred = X_b @ beta
print("\n=== Prediksi (y_pred) ===")
print(y_pred)

# === 6. Bandingkan dengan nilai aktual ===
print("\n=== Nilai Aktual (y) ===")
print(y)
