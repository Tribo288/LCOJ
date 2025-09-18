import math
c=int(input())
op=[]
for i in range(c):
    s=0
    n=int(input())
    for i in range(1,math.isqrt(n)+1):
        if n%i==0:
            s+=i
            if i != n // i:   # tránh cộng trùng khi i^2 = n
                s += n // i
    op.append(s)
for i in op:
    print(i)