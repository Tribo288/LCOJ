def cal(n):
    val=(2+1**0.5)**0.5
    for i in range(-n,-2):
        val=(n+i+val)**0.5
    return val 
if __name__=='__main__':
    T=int(input())
    OP=[]
    for i in range(T):
        n=int(input())
        OP.append(cal(n))
    for i in OP:
        print(i)