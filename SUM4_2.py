def tinh_mau(x):
    return ((1+x)*x)/2
num=int(input())
op=[]
for i in range(num):
    n=int(input())
    S=0
    for i in range(1,n+1):
        S+=1/tinh_mau(i)
    op.append(S)
for i in op:
    print("{:.8f}".format(i))
    
