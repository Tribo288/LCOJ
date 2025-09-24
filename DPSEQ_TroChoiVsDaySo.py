N,K=list(map(int,input().split()))  #K=step
num_ls=[int(i) for i in input().split()]
m=0

# 5 2
#-2 3 -6 -4 5
#=>4
#m=3 ar=3 -6 -4 5
#m=4 ar= -4 5

#
while len(num_ls)>K:
    So_lon_nhat_day_con=max(num_ls[1:K+1])
    m+=So_lon_nhat_day_con
    num_ls=[num_ls.index(So_lon_nhat_day_con)]
print(m)
    