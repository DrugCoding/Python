lis = list(map(int, input().split()))
lis.sort()
a = lis[0] + lis[1]
b = lis[2] + lis[3]
print(b - a)