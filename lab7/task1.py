numbers=[number for number in input().split() ]
copy=numbers.copy()
for x in range(len(copy)):
    if int(copy[x])<0: copy[x] = '0'

print(f'Исходные остатки: {numbers}')
print(f'Исправленные остатки: {copy}')