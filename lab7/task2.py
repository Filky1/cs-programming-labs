numbers=[number for number in input().split()]
numbers=[int(number) for number in numbers]
sq=[]
for x in range(len(numbers)):
    if numbers[x]>0 and numbers[x]%2!=0: sq.append(numbers[x]**2)
print(f'Квадраты: {sq}')