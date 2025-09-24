if __name__=='__main__':
    T=int(input())
    op=[]
    
    #1=1 #2=1+2  #3=3+3 
    for i in range(T):
        n=int(input())
        
        ar=[0.0]*(n+1)
        ar[0]=1
        ar[1]=1
        for i in range(2,n+1):
            ar[i]=ar[i-1]+i
        
        op.append(sum(1/(n)for n in ar))
    for i in op:
        print("{:.8f}".format(i))