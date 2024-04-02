def transpose_matrix(matrix):
    transposed = []
    # Iterate over columns of original matrix
    for i in range(len(matrix[0])):
        # Initialize a new row for the transposed matrix
        new_row = []
        # Iterate over rows of original matrix
        for j in range(len(matrix)):
            # Append the element at (j, i) to the new row
            new_row.append(matrix[j][i])
        # Append the new row to the transposed matrix
        transposed.append(new_row)
    return transposed 