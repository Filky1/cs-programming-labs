n=int(input())
def dels(n):
    mn=[]
    for i in range(1,n+1):
        if n%i==0:
            mn.append(i)
    return set(mn)
print(dels(n))
if len(dels(n))<=2:
    print("Простое")
else: print("Не простое")
        
