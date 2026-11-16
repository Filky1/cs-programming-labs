xy=[x for x in input().split()]
list=[]
stroki=[]
stolbi=[0] * int(xy[1])
for i in range(int(xy[0])):
    list.append(input().split())
for x in list:
    for y in range(len(x)):
        x[y]=int(x[y])
for x in range(int(xy[0])):
    stroki.append(sum(list[x]))
for x in range(int(xy[0])):
    for y in range(int(xy[1])):
        stolbi[y] += list[x][y]

print("Суммы строк:", stroki)
print("Суммы столбцов:", stolbi)
        







