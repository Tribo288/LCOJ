def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0: return False
    return True
x=int(input(),)
if x<10**6:
    for i in range(2,x+1):
        if prime(i):
            print(i,end=" ")