def matrix(ar,row,col):
    return [ar[col*n:(n+1)*col] for n in range(row)]
if __name__=="__main__":
    m,n,i=list(map(int,input().split()))
    ar=[int(i) for i in input().split()]
    my_mt=matrix(ar,m,n)
    sort_col=[]
    for x in range(m):
        sort_col.append(my_mt[x][i-1])
    sort_col=sorted(sort_col)
    for x in range(m):
        my_mt[x][i-1]=sort_col[x]
    for i in my_mt:
        print(*i)
