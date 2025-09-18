def prime(n):
    if n<1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
if __name__=="__main__":
    T=int(input())
    op=[]
    for i in range(T):
        L,F=list(map(int,input().split()))
        op.append([i for i in range(L,F+1) if prime(i)])
    for i in op:
        print(*i)
            