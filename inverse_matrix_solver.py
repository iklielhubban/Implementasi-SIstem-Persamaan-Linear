import numpy as np

def solve_linear_eq_inverse_matrix(A, b):
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, b)
    return x