n=int(input())
bz=0
dz=0
z=0
for i in range(n):
    t=float(input())
    if t<0: dz+=1
    elif t>0: bz+=1
    elif t==0: z+=1
print('Ниже нуля:',dz)
print('Равны нулю:',z)
print('Выше нуля:',bz)