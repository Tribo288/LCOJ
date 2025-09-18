import sys

for line in sys.stdin:
    n = line.strip()
    if not n:  # bỏ qua dòng trống
        continue
    if n[0] == n[-1]:
        print("YES")
    else:
        print("NO")