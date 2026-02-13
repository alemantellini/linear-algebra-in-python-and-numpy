# EJERCICIO 6 - determinants and inverses
import numpy as np

matrix = [[1, 2], [3, 4]]
array = np.array(matrix)

def determinant(matrix, mode="pure"):
    """
    Computes the determinant of a square matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to compute determinant.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The determinant value.
    """
    if mode == "pure":
       return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    elif mode == "numpy":
        return np.linalg.det(matrix)
    else:
        return "Invalid mode"


def inverse_matrix(matrix, mode="pure"):
    """
    Computes the inverse of a square matrix.

    Parameters:
    - matrix: list of lists or np.array -> Matrix to compute inverse.
    - mode: str -> "pure" for Python lists, "numpy" for NumPy arrays.

    Returns:
    - The inverse matrix or a message if it doesn't exist.
    """

    if mode == "pure":
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        if det == 0:
            return "Matrix is not invertible"
        return [[matrix[1][1] / det, -matrix[0][1] / det], 
                [-matrix[1][0] / det, matrix[0][0] / det]]
    elif mode == "numpy":
        det = np.linalg.det(matrix)
        if det == 0:
            return "Matrix is not invertible"
        return np.linalg.inv(matrix)
    else:
        return "Invalid mode"

print(determinant(matrix, "pure"))
print(determinant(matrix, "numpy"))

print(inverse_matrix(matrix, "pure"))
print(inverse_matrix(matrix, "numpy"))
