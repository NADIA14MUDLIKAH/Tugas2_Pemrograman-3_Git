from matrix import Matrix

def Find_determinant(matrix: Matrix):
    """Hitung determinan matriks persegi (rekursif, cocok untuk n kecil)."""
    if matrix is None or matrix.rows != matrix.cols:
        raise ValueError("Hanya matriks persegi yang punya determinan.")
    m = matrix.data
    n = matrix.rows
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    def det(mat):
        size = len(mat)
        if size == 1:
            return mat[0][0]
        if size == 2:
            return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        total = 0
        for col in range(size):
            minor = [row[:col] + row[col+1:] for row in mat[1:]]
            sign = (-1) ** col
            total += sign * mat[0][col] * det(minor)
        return total

    return det(m)
