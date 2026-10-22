def matrixStructure(matrix_size, starting_pos=(0, 0), wall_char="#"):
    matrix = [["#" for _ in range(matrix_size)] for _ in range(matrix_size)]
    matrix[starting_pos[0]][starting_pos[1]] = " "
    return matrix
