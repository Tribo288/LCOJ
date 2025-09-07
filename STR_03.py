from collections import Counter
n=Counter(input().lower())
T=int(input())
O=[]
for i in range(T):
    s=input().lower()
    O.append(n[s])
for i in O:
    print(i)
