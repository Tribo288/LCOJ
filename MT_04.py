def matrix(lst,row,col):
    return[lst[i*col:(i+1)*col]for i in range(row)]
m,n,i=map(int,input().split())
lst=[int(i) for i in input().split()]
mt=matrix(lst,m,n)
mt[i-1]=sorted(mt[i-1])
for i in mt:
    print(*i)