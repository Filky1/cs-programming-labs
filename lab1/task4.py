seconds=int(input("Введите продолжительность поездки:"))
hour=seconds//3600
minutes=(seconds-(hour*3600))//60
seconds1=seconds-(hour*3600+minutes*60)
print(f'{hour:02d}:{minutes:02d}:{seconds1:02d}')
