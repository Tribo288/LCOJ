def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
op=[]
T=int(input())
num=[int(i) for i in input().split()]
for i in num:
    op.append(factorial(i))
for i in op:
    print(i)