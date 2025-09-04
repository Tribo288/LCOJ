def uoc(n):
    if n<=1: return "NO"
    if sum([i for i in range(1,n) if n%i==0])==n: return "YES"
    return "NO"
print(uoc(int(input(": "))))
