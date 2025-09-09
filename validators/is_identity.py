from matrix import Matrix

def is_identity(matrix: Matrix) -> bool:
    """
    Periksa apakah matrix adalah matriks identitas.
    Syarat: matriks persegi, diagonal == 1, selain diagonal == 0.
    """
    if matrix is None or matrix.rows != matrix.cols:
        return False

    n = matrix.rows
    for i in range(n):
        for j in range(n):
            expected = 1 if i == j else 0
            if matrix.data[i][j] != expected:
                return False
    return True
