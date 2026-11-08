n = int(input())

if n < 2:
    print("Ошибка")
else:
    d = 2
    factors = []
    temp = n
    while d <= temp:
        if temp % d == 0:
            factors.append(str(d))
            temp //= d
        else:
            d += 1
    print(" ".join(factors))