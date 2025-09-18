from bisect import bisect_left
def len_lst(lst):
    tails=[]
    for x in lst:
        i=bisect_left(tails,x)