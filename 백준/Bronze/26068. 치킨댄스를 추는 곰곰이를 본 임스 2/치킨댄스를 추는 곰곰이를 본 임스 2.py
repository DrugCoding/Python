a = int(input())
lis = []
for _ in range(a):
    lis.append(input()[2:])
lis2 = []
for i in lis:
    if int(i) <= 90:
        lis2.append(i)
print(len(lis2))