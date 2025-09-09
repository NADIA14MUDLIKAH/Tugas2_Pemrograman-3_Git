from matrix import Matrix

def Is_square(matrix: Matrix) -> bool:
    """Periksa apakah matrix persegi."""
    if matrix is None:
        return False
    return matrix.rows == matrix.cols

def Is_symmetric(matrix: Matrix) -> bool:
    """Periksa apakah matrix simetris."""
    if matrix is None or matrix.rows != matrix.cols:
        return False
    n = matrix.rows
    for i in range(n):
        for j in range(i, n):
            if matrix.data[i][j] != matrix.data[j][i]:
                return False
    return True
