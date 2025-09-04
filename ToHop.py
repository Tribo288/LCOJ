def factorial(x):
    if x==0 or x==1: return 1
    else: return x*factorial(x-1)
def tohop(k,n):
    return(int(factorial(n)/(factorial(k)*factorial(n-k))))
a=int(input("Nhap k: "))
b=int(input("Nhap n: "))
print(tohop(a,b))