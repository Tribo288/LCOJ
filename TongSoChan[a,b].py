def scatb(x):
    return sum([i for i in range(x[0],x[1]+1) if i%2==0])
ip=[int(i) for i in input("Nhap So").split()]
print(scatb(ip))
