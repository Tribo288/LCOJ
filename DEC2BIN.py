#cách 1 dùng bin()
#cách 2 toán thuần túy

n=int(input("Nhap so o thap phan: "))
b=""
if n==0: b="0"
while n>0:
    if n%2!=0: b="1"+b
    else: b="0"+b
    n=n//2
print(b)

#ko chia het 2 thi them 1 vao truoc day bin, neu chia het cho 2 thi them 0 vao truoc day bin
#  