A=[int(i) for i in input(":").split()]
m=0
for i in range(-len(A),0):
    if A[i]>=m: 
        m=A[i]
        o=i     
print(len(A)+o)
#for i in range(-len(A),-1):