import math
tu,mau=[int(i)for i in input().split()]
uc=math.gcd(tu,mau)
if mau<0:
    mau,tu=-mau,-tu
if mau==0:
    print("INVALID")
elif tu%mau==0:
    print(int(tu/mau))
else:
    print(int(tu/uc),int(mau/uc))
    