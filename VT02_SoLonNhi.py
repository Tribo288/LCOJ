from collections import Counter
n=int(input())
A=list(map(int,input().split()))
#A=[int i for i in input("Nhap Mang A").split()
ls=sorted(Counter(A))
if len(ls)>1:
    print(ls[-2])
else:
    print("NOT FOUND")
