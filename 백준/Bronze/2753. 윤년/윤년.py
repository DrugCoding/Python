a = int(input())

if not a%100 == 0 and a%4 == 0:
    print("1")

elif a%400 == 0:
    print("1")
    
else:
    print("0")