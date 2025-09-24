import sys
import math
imput=sys.stdin.readline
max_n=10**6
#prefix:
dp=[0.0]*(max_n+1)   #tap 1 list co do dai den max_n+1
dp[1]=1
for i in range(2,max_n+1):
    dp[i]=math.sqrt(i+dp[i-1])   #O(n)
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        print("{:.5f}".format(dp[n]))