DauVao=list(map(int,input().split()))
NChuVi=sum(i for i in DauVao)/2
DienTich=(NChuVi*(NChuVi-DauVao[0])*(NChuVi-DauVao[1])*(NChuVi-DauVao[2]))**0.5
if (DauVao[0]+DauVao[1])>DauVao[2]:
  print("{:.2f}".format(NChuVi*2),"{:.2f}".format(DienTich))
else:
  print("NO")
