from matrix_regression.matrix import Matrix

# Membaca matriks dari file CSV
csv_path = "data/suhu.csv"  # sesuaikan kalau file di folder lain
m = Matrix.from_csv(csv_path)

print("=== Matriks dari CSV ===")
print(m)

print("\n=== Transpose ===")
print(m.transpose())

print("\n=== Inverse ===")
try:
    print(m.inverse())
except Exception as e:
    print(f"Tidak bisa dihitung invers: {e}")
