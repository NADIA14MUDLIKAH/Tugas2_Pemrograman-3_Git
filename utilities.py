Python
# matriks/utilities.py
def print_matrix(matrix):
    """
    Mencetak isi dari objek matriks.
    """
    for row in matrix.data:
        print(row)

# utilities.py: API kompatibilitas, mem-forward ke modul terpisah
from utilities_package.validators import Is_square, Is_symmetric
from operations.determinant import Find_determinant

__all__ = ["Is_square", "Is_symmetric", "Find_determinant"]
