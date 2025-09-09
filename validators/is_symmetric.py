from matrix import Matrix

def is_symmetric(matrix: Matrix) -> bool:
    """
    Periksa apakah matrix adalah matriks simetris.
    Syarat: matriks harus persegi dan matrix.data[i][j] == matrix.data[j][i] untuk semua i,j.
    """
    if matrix is None or matrix.rows != matrix.cols:
        return False

    n = matrix.rows
    for i in range(n):
        for j in range(i, n):  # mulai dari i untuk efisiensi
            if matrix.data[i][j] != matrix.data[j][i]:
                return False
    return True
