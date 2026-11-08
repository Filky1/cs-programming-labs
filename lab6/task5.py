n = int(input())

if n < 1 or n > 10:
    print("Ошибка")
else:
    for i in range(n):
        row = []
        for j in range(n):
            # Расстояние равно большей координате минус меньшая
            if i > j:
                row.append(str(i - j))
            else:
                row.append(str(j - i))
        print(" ".join(row))
