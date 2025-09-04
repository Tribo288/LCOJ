import math 
a,b=map(int,input(" Nhap Tu va mau: ").split())
if b==0: print("Khong the rut gon")
if b<0: a=-a; b=-b
ucln=math.gcd(a,b)
print(int(a/ucln),int(b/ucln))