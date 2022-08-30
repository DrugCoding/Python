n = int(input())
lis = []
for i in reversed(range(n+1)):
    lis.append(i)
    
print(*lis)