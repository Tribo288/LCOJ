#array to matrix
def matrix(ls,row,col):
    return [ls[i*col:(i+1)*col]for i in range(row)]
if __name__=='__main__':
    m,n=list(map(int,input().split()))
    ls=[i for i in input().split()]
    op=matrix(ls,m,n)
#1 2 3    4 5 6   7 8 9
#0 1 2    3 4 5   6 7 8
#[[1, 2, 3], 0:2
# [4, 5, 6], 3:5
# [7, 8, 9]   6:8
for i in op:
    print(*i)