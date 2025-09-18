T=int(input())
op=[]
def cal(n):
    value=1
    for i in range(n):
        value=1/(1+value)
    return value
if __name__=='__main__':
    for i in range(T):
        n=int(input())
        op.append(("{:.5f}".format(cal(n))))
    for i in op:
        print(i)