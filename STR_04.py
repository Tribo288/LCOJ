from collections import Counter
import string
st=Counter(input().lower())
ls=sorted(st)
for i in ls:
    if i in list(string.ascii_letters) or i in range(10):
        print(f"{i} {st[i]}")       