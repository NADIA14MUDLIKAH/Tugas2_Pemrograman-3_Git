def divide_matrices(matrix1, matrix2):
    # BUG: Tidak ada validasi dimensi
    result_data = [[matrix1.data[i][j] / matrix2.data[i][j]
                    for j in range(matrix1.cols)]
                    for i in range(matrix1.rows)]
    return type(matrix1)(result_data)
