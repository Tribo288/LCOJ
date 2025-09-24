T=int(input())
op=[]
for i in range(T):
    n=int(input())
    op.append(sum(1/i for i in range(1,n+1)))
for i in op:
    print("{:.5f}".format(i))