a,b=[int(i) for i in input().split()]
if a==0 and b !=0:
    print("NO")
elif a==0 and b==0:
    print("WOW")
else:
    print("{:.2f}".format(-b/a))