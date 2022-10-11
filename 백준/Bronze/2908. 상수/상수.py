a, b = map(str, input().split())
a = a[::-1]
b = b[::-1]
lis = []
lis.append(a)
lis.append(b)
print(max(lis))