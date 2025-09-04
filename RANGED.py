A,B,C,D=map(int,input().split())
if (B>=C and D>=A) or (A<=D and B>=C):
  print("YES")
else:
  print("NO")
