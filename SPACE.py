n=int(input())
op=[]
for i in range(n):
    s=input()
    count=0
    if s[-1] ==" ":
            count+=1    
    for i in range(0,len(s)-1):
        if s[i]==" " and s[i+1] != " ":
            count+=1
    op.append(count)
for i in op:
    print(i)
