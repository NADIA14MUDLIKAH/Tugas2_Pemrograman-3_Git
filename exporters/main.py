# matriks/main.py
# ... (kode impor lainnya)
from exporters.csv_exporter import export_to_csv
if __name__ == "__main__":
    # ... (kode demonstrasi lainnya)
    matrix_c = Matrix([[10, 20], [30, 40]])
    print("\nMenyimpan Matriks C ke file CSV:")
    export_to_csv(matrix_c, "matriks_c.csv")
