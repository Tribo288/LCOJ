import math
def prime(i):
    if i<2:
        return False
    else:
        for x in range(2,int(math.isqrt(i))+1):
            if i%x==0:
                return False
    return True
n=int(input())
if prime(n):
    print("YES")
else:
    print("NO")