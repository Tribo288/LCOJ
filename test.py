T=int(input())  
op=[]
for i in range(T):
    o=int(input())
    op.append("{:.5f}".format(sum((2*i-1)**0.5 for i in range(1,o+1))))
for i in op:
    print(i)
