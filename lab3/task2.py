fio=str(input("Введите ФИО:"))
surname=fio[0:fio.find(' ')]
name=fio[fio.find(' ')+1:fio.rfind(' ')]
middlename=fio[fio.rfind(' ')+1:]
surname=surname[0].upper()+surname[1:].lower()
print(surname,name[0].upper()+'.',middlename[0].upper()+'.')