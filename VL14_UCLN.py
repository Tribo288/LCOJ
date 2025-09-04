def timuoc(n):
    return [x for x in range(1,n+1) if n%x==0]
a=int(input("Nhap a: "))
b=int(input("Nhap b: "))
t=timuoc(a)
ln=max(timuoc(a))
if ln in timuoc(b):
    print(ln)
else: t.remove(ln)
print(ln)


#Euclid Agorithm
def divisor(n):
    while b!=0:
        a,b=b,a%b
    return abs(a)


#M math function
import math
math.gcd(10,30) 
