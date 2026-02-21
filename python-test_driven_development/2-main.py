#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Test 1: div=3
print(matrix_divided(matrix, 3))
print(matrix)  # original matrix dəyişmir

# Test 2: div=2
print(matrix_divided([[2, 4], [6, 8]], 2))

# Test 3: empty matrix
print(matrix_divided([[]], 1))
