import math
def matrix(lst,row,col):
    return [lst[col*n:(n+1)*col] for n in range(row)]
if __name__=="__main__":
    n=int(input())
    ar=list(map(int,input().split()))
    my_ar=matrix(ar,n,n)
    print(sum(my_ar[i][i] for i in range(n)))
