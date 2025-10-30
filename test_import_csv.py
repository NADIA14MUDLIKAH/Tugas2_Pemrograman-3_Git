from matrix_regression.matrix import Matrix

# Import matriks dari file CSV
m = Matrix.from_csv("data/matriks.csv")

print("Matriks hasil impor:")
print(m)

# Operasi lanjut
print("\nTranspose:")
print(m.transpose())

# Kalau mau inverse, pastikan matriks bujur sangkar
