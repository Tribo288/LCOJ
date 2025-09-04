def tong(x):
    return int((x+1)*x/2)
print(tong(int(input("bai1:"))))
def tong2(x):
    return int((x+2)*(x-1)/2+2*x)
print(tong2(int(input("bai: "))))
def tong3(x):
    return sum([i**-1 for i in range(2,x+1)])
print(tong3(int(input("bai3:"))))

#bai4  
#1 − 2 + 3−4+5-6+7. . . +(3n + 1), nếu n chẵn.
#1 − 2 + 3−. . . −(3n + 1), nếu n lẻ
#n=2 3n+1=7
#1-2+3-4+5-6+7
#n=3 3n+1=10
#1-2+3-4+5-6+7-8+9-10
def tong4(n):
    return sum(i if i%2!=0 else -i for i in range(1,3*n+2))
print(tong4(int(input("Bai4:"))))
