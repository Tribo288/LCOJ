import sys
from bisect import bisect_left
def len_lst(lst):
    tails=[]
    for x in lst:
        i=bisect_left(tails,x)
        if i==len(tails):
            tails.append(x)
        else:
            tails[i]=x
    return len(tails)
if __name__=="__main__":
    input=sys.stdin.read().strip().split()
    n=int(input[0])
    ar=list(map(int,input[1:n+1]))
    print(len_lst(ar))