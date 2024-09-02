def bubble_sort_row(matrix, row_index):
    """Ordena una fila especIfica de la matriz en orden ascendente usando Bubble Sort."""
    row_length = len(matrix[row_index])
    for i in range(row_length):
        for j in range(0, row_length - i - 1):
            if matrix[row_index][j] > matrix[row_index][j + 1]:
                # Intercalation los elementos
                matrix[row_index][j], matrix[row_index][j + 1] = matrix[row_index][j + 1], matrix[row_index][j]

# Matriz 3x3 de ejemplo
matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matriz original:")
for row in matrix:
    print(row)

# Ordena la segunda fila (índice 1)
bubble_sort_row(matrix, 1)

print("\nMatriz con la segunda fila ordenada:")
for row in matrix:
    print(row)
