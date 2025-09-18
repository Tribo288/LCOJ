def cal(n):
    val=0
    for i in range(n):
        val=(2+val)**0.5
    return val
        
T=int(input())
OP=[]
for i in range(T):
    n=int(input())
    OP.append(cal(n))
for i in OP:
    print("{:.5f}".format(i))
    
