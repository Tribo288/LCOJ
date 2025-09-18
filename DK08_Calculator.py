a,op,c=list(map(str,input().split()))
a,c=float(a),float(c)
if op=="+":
    print("{:.2f}".format(a+c))
elif op=="-":
    print("{:.2f}".format(a-c))
elif op=="*":
    print("{:.2f}".format(a*c))
elif op=="/":
    if c==0 or abs(a)>10000 or abs(c)>10000:
        print("Math Error")
    else:
        print("{:.2f}".format(a/c))
        