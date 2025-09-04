def namnhuan(x):
    if x<0: return print("INVALID")
    elif (x%4==0 and x%100!=0) or (x%400==0):return print("YES") 
    else: return print("NO")
print(namnhuan(int(input())))


#Giai thich:
# Nam nhuan co the la nam khong tron thế kỉ và chia hết cho 4 hoặc năm tròn thế kỉ và chia hết cho 400