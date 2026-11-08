total=[]
count=0
while True:
    price=str(input())
    if price == 'stop': break
    price=int(price)
    count+=1
    total.append(price)
print('Покупок:',count)
print('Общая стоимось:',sum(total))
print(f'Средняя стоимость: {(sum(total)/len(total)):.2f} руб')