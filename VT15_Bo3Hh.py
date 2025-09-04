#VT15
n=int(input())
ls=list(map(int, input().split()))
op=sorted(ls)
s=1
print(max(op[-1]*op[-2]*op[-3],op[-n]*op[-n+1]*op[-1]))