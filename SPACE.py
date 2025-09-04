n=int(input())
op=[]
for i in range(n):
    st=input()
    c=0
    for x in range(1,len(st)):
        if st[x]==" " and (st[x+1]!=" " or st[x-1]!=" "):
            c+=1
    op.append(c)
print(*[op])

#__ab___
#_ab
#a_b
#len=7