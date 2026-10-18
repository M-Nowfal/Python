# PROGRAM 10 – Program to perform all possible matrix operations using numpy libraries.

import numpy as np

matrix_A = np.array([
  [2, 4, 6],
  [1, 5, 9],
  [8, 3, 7]
])

matrix_B = np.array([
  [1, 2, 3],
  [5, 4, 4],
  [8, 6, 1]
])

print("....Initial Matrices....")

print("Matrix A:\n", matrix_A)

print("Matrix B:\n", matrix_B)

print("\n...Basic Arithmetic (element-wise)...")

add_result = np.add(matrix_A, matrix_B)

matrix_A + matrix_B

print("Matrix Addition (A+B):\n", add_result)

sub_result = np.subtract(matrix_A, matrix_B)

matrix_A - matrix_B

print("Matrix Subtraction(A-B):\n", sub_result)

elem_mult = np.multiply(matrix_A, matrix_B)

matrix_A * matrix_B

print("Element-wise Multiplication (A*B):\n", elem_mult)

elem_div = np.divide(matrix_A, matrix_B)

print("Element-wise Division (A/B):\n", elem_div)

scalar_mult = matrix_A * 2

print("Scalar Multiplication (A*2):\n", scalar_mult)

print("\n Matrix Multiplication & Manipulations")

matrix_mult = np.dot(matrix_A, matrix_B)

print("True Matrix Multiplication (A@B):\n", matrix_mult)

transpose_A = matrix_A.T

np.transpose(matrix_A)

print("Transpose of Matrix A:\n", transpose_A)

trace_A = np.trace(matrix_A)

print("Trace of Matrix A:", trace_A)

matrix_float = np.identity(3)

print("3x3 float Identity matrix:")

print(matrix_float)

matrix_int = np.identity(4, dtype=int)

print("\n4x4 integer identity matrix:")

print(matrix_int)

print("\nAdvanced Linear Algebra Operations")

det_A = np.linalg.det(matrix_A)

print("Determinant of Matrix A:", det_A)

try:
  inverse_B = np.linalg.inv(matrix_B)
  print("Inverse of Matrix B:\n", inverse_B)

except np.linalg.LinAlgError:
  print("Matrix B is singular & cannot be inverted.")
