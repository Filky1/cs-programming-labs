info=str(input("Введите код документа:"))
country=info[0:3]
year=info[4:8]
number=info[9:13]
print(f'Категория: {country}')
print(f'Год: {year}')
print(f'Номер: {number}')
unnumber=number[::-1]
print(f'Обратный номер: {unnumber}')
