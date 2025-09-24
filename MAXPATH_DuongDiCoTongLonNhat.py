import sys
input=sys.stdin.readline
if __name__=="__main__":
    m,n=map(int,input().split())
    ar=[list(map(int,input().split())) for i in range(m)]
    dp=[[-10**9]*n for i in range(m)]
    #tao cot 0 de tham chieu
    for i in range(m):
        dp[i][0]=ar[i][0]
        
    #tinh cac cot
    for y in range(1,n):  #colums
        for x in range(m):   # rows
            best_prev=dp[x][y-1]
            if x>0:  #loai hang dau ko dc di len
                best_prev=max(best_prev,dp[x-1][y-1])
            if x<(m-1): #loai hang cuoi ko dc di xuong
                best_prev=max(best_prev,dp[x+1][y-1])
            dp[x][y]=ar[x][y]+best_prev
            
    print(max(dp[i][n-1] for i in range(m)))