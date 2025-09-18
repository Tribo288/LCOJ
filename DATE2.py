t=int(input())
mins=t/60
hour=mins/60
sec=t-60*mins-hour*60*60
print(f"{hour}:{mins}:{sec}")
