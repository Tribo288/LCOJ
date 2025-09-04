#VL09
def factorial(n):
    if n==0 or n==1: return 1
    return n*factorial(n-1)
def tong(n):
    return sum([(n[0]**i)/(factorial(i)) for i in range(1,n[1]+1)])
ip=[int(i) for i in input("Nhap x va n: ").split()]
print(round(tong(ip),2))