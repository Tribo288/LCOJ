T=int(input())
op=[]
def cal(n):
    return sum(i for i in range(1,n+1))
if __name__=='__main__':
    for i in range(T):
        n=int(input())
        op.append(sum(1/cal(i) for i in range(1,n+1)))
    for i in op:
        print(op)