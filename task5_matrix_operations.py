# Task 5: Two list comprehensions on a square matrix:
#   1. Primary diagonal (top-left to bottom-right)
#   2. Flattened list of only the even numbers

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

diagonal = [matrix[i][i] for i in range(len(matrix))]

evens = [num for row in matrix for num in row if num % 2 == 0]

print("Diagonal:", diagonal)  # [1, 5, 9]
print("Evens:", evens)        # [2, 4, 6, 8]
