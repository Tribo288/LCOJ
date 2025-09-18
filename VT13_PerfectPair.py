n=int(input())
ls=[int(i) for i in input().split()]
max=ls[0]+ls[-1]
daura=[ls[-1],ls[0]]
for i in range(1,len(ls)-1):
    if ls[i]+ls[i+1]>=max:
        max=ls[i]+ls[i+1]
        daura[0],daura[1]=ls[i],ls[i+1]
print(*daura)