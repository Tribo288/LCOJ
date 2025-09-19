#tinh n can - di 2 can co cuo
import math
op=[]
if __name__=="__main__":
    T=int(input())
    for i in range(T):
        n=int(input())
        s=math.sqrt(n)
        for x in range(n-1,0,-1):
            s=math.sqrt(abs(x)+s)
        op.append(s)
    for i in op:
        print("{:.5f}".format(i))