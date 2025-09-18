N=int(input())
lst=list(map(int,input().split()))
m=max(lst)
op=0
for i in range(len(lst)):
    if lst[i]==m:
        op=i 
print(op)   
 