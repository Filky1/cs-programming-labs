fio=str(input("Введите ФИО:"))
fio=fio.split()
surname=fio[0]
surname=surname[0].upper()+surname[1:].lower()
name=fio[1][0].upper()
otchestvo=fio[2][0].upper()
print(surname,name+'.',otchestvo+'.')