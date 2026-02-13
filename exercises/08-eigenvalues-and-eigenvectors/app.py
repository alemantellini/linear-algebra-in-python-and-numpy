# EJERCICIO 8 - eigenvalues and eigenvectors
import numpy as np  

def compute_eigen(A, mode="numpy"):
    """
    Computes the eigenvalues and eigenvectors of a square matrix.

    Parameters:
    - A: list of lists or np.array -> Square matrix.
    - mode: str -> "pure" for manual calculation, "numpy" for np.linalg.eig().

    Returns:
    - List of eigenvalues (and eigenvectors if mode="numpy").
    """

    # Verificar si es cuadrada
    if len(A) != len(A[0]):
        return "Matrix must be square"
    
    if mode == "pure":
        # Solo soportamos 2x2
        if len(A) != 2:
            return "Pure mode only supports 2x2 matrices"
        
        a, b = A[0]
        c, d = A[1]

        trace = a + d
        determinant = a*d - b*c
        discriminant = trace**2 - 4*determinant

        lambda1 = (trace + discriminant**0.5) / 2
        lambda2 = (trace - discriminant**0.5) / 2

        return [lambda1, lambda2], None
    
    elif mode == "numpy":
        A_np = np.array(A)

        if A_np.shape[0] != A_np.shape[1]:
            return "Matrix must be square"

        eigenvalues, eigenvectors = np.linalg.eig(A_np)

        # Ordenar de mayor a menor
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        return eigenvalues, eigenvectors

    else:
        return "Invalid mode"
    
# Matriz de ejemplo
A = [[3, 2], [1, 4]]
print("Autovalores manuales:", compute_eigen(A, mode="pure"))

eigenvalues, eigenvectors = compute_eigen(A, mode="numpy")
print("Autovalores:", eigenvalues)
print("Autovectores (como columnas):")
print(eigenvectors)
