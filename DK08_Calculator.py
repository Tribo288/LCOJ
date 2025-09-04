ip=input().split()
#vd: 1 + 1 
#lam tron 2 stp
try:
    if ip[2]==0: print("Math Error")
    if ip[1]=="+":
        print("{:.2f}".format(int(ip[0])+int(ip[2])))
    elif ip[1]=="-":
        print("{:.2f}".format(int(ip[0])-int(ip[2])))
    elif ip[1]=="*":
        print("{:.2f}".format(int(ip[0])*int(ip[2])))
    else:
        print("{:.2f}".format(int(ip[0])/int(ip[2])))
except:
    print("Math Error")