year=int(input())
if year<=0 or year>=10000: print("Ошибка")
elif year%400==0 or (year%4==0 and year%100!=0):
    print("Високосный")
else: print("Невисокосный")
