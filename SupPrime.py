#Số siêu nguyên tố là số mà tất cả các chữ số của nó đều là snt
def prime(n):
    n=int(n)
    if n<1: return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return False
    return True
n=int(input("So CHu so"))
op=[]
for i in range(2,10**n):
    count=0
    for x in range(0,len(str(i))):
        if prime(str(i)[x])==True:
            count+=1
    if prime(i)==True and count==len(str(i)):
        op.append(i)
print(*op)

