number=str(input('Введите номер телефона:'))
number=number.replace('+','').replace('-','').replace(' ','').replace('(','').replace(')','')
print(number)