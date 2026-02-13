# EJERCICIO 5 - matrix transposition
import numpy as np  
matrix = [[1, 2, 3], [4, 5, 6]]
def transpose(matrix, mode="pure"):
    """
    Computes the transpose of a matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to transpose.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The transposed matrix.
    """

    if not matrix or any(len(row) != len(matrix[0]) for row in matrix):
        return "Invalid matrix"
    if mode == "pure":
        transpuesta = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return transpuesta
    elif mode == "numpy":
        A = np.array(matrix)
        transpuesta = A.T
        return transpuesta

print(transpose(matrix, "pure"))
print(transpose(matrix, "numpy"))
