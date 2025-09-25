def matrix(lst,row,col):
    return [lst[col*n:col*(n+1)] for n in range(row)]
if __name__=="__main__":
    m,n=list(map(int,input().split()))
    A=list(map(int,input().split()))
    my_lst=matrix(A,m,n)
    s=0
    for i in range(len(my_lst)):
        if i%2!=0:
            s+=sum(my_lst[i])
    print(s)
