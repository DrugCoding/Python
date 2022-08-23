a = int(input())
b = int(input())
c = int(input())
d = a * b * c
lis = list(str(d))

for i in range(10):
    print(lis.count(str(i)))