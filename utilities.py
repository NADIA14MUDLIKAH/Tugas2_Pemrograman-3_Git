Python
# matriks/utilities.py
def print_matrix(matrix):
    """
    Mencetak isi dari objek matriks.
    """
    for row in matrix.data:
        print(row)
# tambahan sementara sebelum refactor
from matrix import Matrix

def Is_square(matrix: Matrix) -> bool:
    """Periksa apakah matrix persegi."""
    if matrix is None:
        return False
    return matrix.rows == matrix.cols

def Is_symmetric(matrix: Matrix) -> bool:
    """Periksa apakah matrix simetris (matrix == transpose(matrix))."""
    if matrix is None or matrix.rows != matrix.cols:
        return False
    n = matrix.rows
    for i in range(n):
        for j in range(i, n):
            if matrix.data[i][j] != matrix.data[j][i]:
                return False
    return True

def Find_determinant(matrix: Matrix):
    """Hitung determinan (simple recursive). Hanya untuk matriks persegi kecil."""
    if matrix is None or matrix.rows != matrix.cols:
        raise ValueError("Hanya matriks persegi yang punya determinan.")
    # convert to plain nested list
    m = matrix.data
    n = matrix.rows
    # basis kecil
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    # fungsi minor untuk rekursif
    def det(mat):
        size = len(mat)
        if size == 1:
            return mat[0][0]
        if size == 2:
            return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        total = 0
        for col in range(size):
            # build minor
            minor = [row[:col] + row[col+1:] for row in mat[1:]]
            sign = (-1) ** col
            total += sign * mat[0][col] * det(minor)
        return total
    return det(m)
