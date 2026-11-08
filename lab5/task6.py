n = int(input())
odd_count = 0
for i in range(n):
    num = 1
    row_items = []
    for j in range(i + 1):
        row_items.append(str(num))
        if num % 2 != 0:
            odd_count += 1
        num = num * (i - j) // (j + 1)
    print(" ".join(row_items))
print(f"Нечетных элементов: {odd_count}")
