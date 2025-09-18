import math
def square_number(n):
    if n<0:
        return False
    elif int(math.isqrt(n))**2==n:
        return True
    return False
if __name__=='__main__':    
    n=int(input())
    if square_number(n):
        print("YES")
    else:
        print("NO")