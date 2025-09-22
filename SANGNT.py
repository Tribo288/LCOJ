def prime_list(n):
    
    is_prime=[True]*(n+1)
    is_prime[0]=is_prime[1]=False
    
    for i in range(2,int(n**0.5)+1):
        if is_prime[i]:
            for x in range(i*i,n+1,i):
                is_prime[x]=False
                
    primes=[i for i,val in enumerate(is_prime) if val]
    return primes
if __name__=="__main__":
    n=int(input())
    print(*prime_list(n))