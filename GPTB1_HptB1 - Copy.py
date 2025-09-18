#ax+by=c
#dx+ey=f

#by=c-ax
#ey=f-dx
#y=(c-ax)/b
#y=(f-dx)/e
#(f-dx)b=(c-ax)e
#fb-dbx=ce-aex
#-dbx+aex=ce-bf

a,b,c,d,e,f=list(map(int,input().split()))
det=a*e-b*d
if det !=0:
    x=(c*e-b*f)/(-d*b+a*e)
    y=(c-a*x)/b
    print("{:.2f}".format(x),"{:.2f}".format(y))
else:
    if a/d==b/e!=c/f:
      print("VONGHIEM")
    elif a/d==b/e==c/f:
      print("VOSONGHIEM")