a=int(input())
b=int(input())
summ=0
prod=1
for i in range(a,b+1):
    summ+=i
    prod=prod*i
print(f'Сумма: {summ}')
print(f'Произведение: {prod}')