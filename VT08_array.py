n=int(input())
ls=list(map(int,input().split()))
#1 3 2 5
#0 1 2 3
#1 3 2 5 4
#0 1 2 3 4
#len=4

for i in range(n):
    if i%2!=0:
        try:
            ls[i]+=abs(ls[i+1]-ls[i-1])
        except:
            ls[i]+=abs(ls[i-1])
print(*ls)