n = int(input())
lis = []
for i in range(n//4):
    lis.append('long')
lis.append('int')
print(*lis)