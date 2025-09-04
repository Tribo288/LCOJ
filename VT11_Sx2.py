n=int(input())
ls=list(map(int,input().split()))
temp=sorted(ls[1:len(ls)-1])
ls[1:len(ls)-1]=temp
print(*ls)