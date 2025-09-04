#THuHOACH
#N C are number of bag and max capacity of truck
#w1 w1 w3...wN is weight of each bag
N,C=map(int,input().split())
w=sorted(list(map(int,input().split())))
while sum(w)>C:
    w.remove(w[0])
print(sum(w))
