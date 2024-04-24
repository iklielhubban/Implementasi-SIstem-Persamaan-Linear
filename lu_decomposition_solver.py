import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = A.copy()

    for i in range(n-1):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j] -= factor * U[i]

    return L, U

def solve_linear_eq_lu_decomposition(A, b):
    L, U = lu_decomposition(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x