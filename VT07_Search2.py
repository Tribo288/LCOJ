lst=list(map(int,input().split()))
Dau_ra=[]
for i in range(len(lst)-1):
    if lst[i]==lst[-1]:
        Dau_ra.append(i+1)
if len(Dau_ra)>0:
    print(*Dau_ra)
else:
    print(-1)