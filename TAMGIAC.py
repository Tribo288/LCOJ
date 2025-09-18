a,b,c=list(map(int,input().split()))
NChuVi=(a+b+c)/2
DienTich=(NChuVi*(NChuVi-a)*(NChuVi-b)*(NChuVi-c))**0.5
if (a+b)>c:
  print(int(NChuVi*2),"{:.2f}".format(DienTich))
else:
  print("NO")

