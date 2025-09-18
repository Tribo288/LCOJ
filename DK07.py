#ax**2+bx+c
import math
a,b,c=list(map(int,input().split()))
delta=b**2-4*a*c
if a==0:
    if b==0 and c!=0:
        print("NO")
    elif b==0 and c==0:
        print("WOW")
    else:
        print("{:.2f}".format(-c/(b)))
elif delta<0:
    print("NO") 
elif delta==0:
    print("{:.2f}".format(-b/(2*a)))
else:
    x1=(-b+math.sqrt(delta))/(2*a)       
    x2=(-b-math.sqrt(delta))/(2*a)
    x1,x2=sorted([x1,x2])
    print("{:.2f}".format(x1),"{:.2f}".format(x2))       