a,b=map(str,input().split())
print(*[chr(x) for x in range(ord(a.upper()),ord(b.upper())+1)])