n=int(input())
ls=list(map(int,input().split()))
#3 2 -1 2 4
#0 1 2 3 4

#1 2 6 1 6 2
#len=6
#0 1 2 3 4 5
TempMax=ls[0]+ls[-1]
Next_Num=ls[0]
Now_Num=ls[-1]
for i in range(1,n-1):
    if ls[i-1]+ls[i]>TempMax or ls[i+1]+ls[i]>TempMax:
        Now_Num==ls[i]
        #NextNum
        if ls[i-1]+ls[i]>ls[i+1]+ls[i]:
            Next_Num=ls[i-1]
            TempMax=ls[i-1]+ls[i]
        else:
            Next_Num=ls[i+1]
            TempMax=ls[i+1]+ls[i]
if Now_Num==ls[-1]:
    print(Now_Num,Next_Num)
else:
    if Now_Num<Next_Num:
        print(Now_Num,Next_Num)
    else:
        print(Next_Num,Now_Num)