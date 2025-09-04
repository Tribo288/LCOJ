n=int(input(": "))
op=[]
if n==0: print("INF")
else:
    for i in range(1,abs(n+1)):
        if n%i==0:
            op.append(i)
            op.append(-i)
for i in sorted(op, reverse=True):
    print(i, end=" ")
