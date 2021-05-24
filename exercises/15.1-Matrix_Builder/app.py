from random import randint

def matrix_builder(n):
    matrix = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(randint(0,1))
        matrix.append(row)
    return matrix

result = matrix_builder(3)
print(result)
