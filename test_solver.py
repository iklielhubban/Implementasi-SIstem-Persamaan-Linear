import numpy as np
from inverse_matrix_solver import solve_linear_eq_inverse_matrix
from lu_decomposition_solver import solve_linear_eq_lu_decomposition
from crout_decomposition_solver import solve_linear_eq_crout_decomposition

# Matriks koefisien dan vektor hasil
A = np.array([[2, 1], [5, 3]])
b = np.array([4, 10])

# Solusi menggunakan metode matriks balikan
x_inverse_matrix = solve_linear_eq_inverse_matrix(A, b)
print("Solusi x (Matriks Balikan):", x_inverse_matrix)

# Solusi menggunakan metode dekomposisi LU Gauss
x_lu_decomposition = solve_linear_eq_lu_decomposition(A, b)
print("Solusi x (Dekomposisi LU Gauss):", x_lu_decomposition)

# Solusi menggunakan metode dekomposisi Crout
x_crout_decomposition = solve_linear_eq_crout_decomposition(A, b)
print("Solusi x (Dekomposisi Crout):", x_crout_decomposition)