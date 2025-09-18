n=int(input())
ls=list(int(i)for i in input().split())
ls=sorted(ls)
min=max(abs(ls[0]-ls[1]),abs(ls[-1]-ls[-2]))
for i in range(2,len(ls)-1):
    if abs(ls[i]-ls[i+1])<min:
        min=abs(ls[i]-ls[i+1])
print(min)