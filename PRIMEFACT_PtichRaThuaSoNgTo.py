import math

#sang NT
def prime_list(n):
    
    lst=[True]*(n+1)
    lst[0]=lst[1]=False
  
    for i in range(2,int(math.sqrt(n))+1):
        if lst[i]:
            for x in range(i*i,n+1,i):
                lst[x]=False
    primes=[ind for ind,val in enumerate(lst) if val]
    return primes

#Main
if __name__=="__main__":
    k=int(input())
    prime_k=prime_list(k)
    op=[]
    for i in prime_k:
        time=0
        while k%i==0:
            k=k/i
            time+=1
            if time==1:
                op.append([i])
            else:
                op.append([i,time])
        prime_k.remove(i)
#10/2 =5
    for i in op:
        print(*i)