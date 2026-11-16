r, c = [int(x) for x in input().split()]
matrix = []
for i in range(r):
    row = [int(x) for x in input().split()]
    matrix.append(row)
row_start, row_end, col_start, col_end = [int(x) for x in input().split()]
target = int(input())
found = False
for i in range(row_start, row_end + 1):
    for j in range(col_start, col_end + 1):
        if matrix[i][j] == target:
            print(i, j)
            found = True
if not found:
    print("Не найдено")
