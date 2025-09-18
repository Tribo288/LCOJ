import math
m,n=list(map(int,input().split()))
mt = [list(map(int, input().split())) for _ in range(m)]
op=set()
for x in range(m):
    for y in range(n):
        if int(math.isqrt(mt[x][y]))**2 == mt[x][y]:
            op.add(mt[x][y])
print(*sorted(op) if op else "NOT FOUND")
