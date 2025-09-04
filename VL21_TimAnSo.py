# 1 + 2 + 3+. . . +x ≤ N
#input=N

#Cach 1
s=0
N=int(input(": "))
for i in range(1,N):
    s+=i
    if s<N:
        m=i
    else: break
print(m)