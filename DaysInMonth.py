def namnhuan(x):
    if (x%4==0 and x%100!=0) or (x%400==0):return True 
    return False
def dayinmonth(m,y):
    if m not in range(1,13) or y not in range(1,10**5):
        print("INVALID")
    elif m==2 and namnhuan(y): return 29
    elif m==2 and not namnhuan(y):return 28
    elif m in [4,6,9,11]: return 30
    else: return 31
l=[int(i) for i in input().split()]
print(dayinmonth(l[0],l[1]))