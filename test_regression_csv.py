from matrix_regression.regression import LinearRegressionMatrix
from matrix_regression.matrix import Matrix

# Import data dari CSV
data = Matrix.from_csv("data/matriks.csv")

# Ambil langsung data numpy-nya
data_np = data.data

# Pisahkan kolom Hari (X) dan Suhu (y)
hari = data_np[:, 0].reshape(-1, 1)  # kolom pertama (independen)
suhu = data_np[:, 1].reshape(-1, 1)  # kolom kedua (dependen)

# Buat model regresi
model = LinearRegressionMatrix(hari, suhu)
model.fit()

# Prediksi suhu untuk hari ke-8
prediksi = model.predict([[8]])
print(f"Prediksi suhu untuk hari ke-8: {prediksi[0][0]:.2f} °C")

