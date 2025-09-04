def atob(ip,op):
    op=[int(i) for i in range(ip[0],ip[1]+1)]
    return op
ip=[int(i) for i in input(': ').split()]
op=[]
print(atob(ip,op).split())

