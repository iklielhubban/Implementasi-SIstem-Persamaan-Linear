import numpy as np

def crout_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        U[j, j] = 1
        for i in range(j, n):
            s1 = sum(U[k, j] * L[i, k] for k in range(j))
            L[i, j] = A[i, j] - s1
        for i in range(j, n):
            s2 = sum(U[k, j] * L[i, k] for k in range(j))
            U[j, i] = (A[j, i] - s2) / L[j, j]

    return L, U

def solve_linear_eq_crout_decomposition(A, b):
    L, U = crout_decomposition(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x