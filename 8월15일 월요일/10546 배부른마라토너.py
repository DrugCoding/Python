a = int(input())
lis = [input() for _ in range(a)]
lis2 = [input() for _ in range(a-1)]
for i in range(a-1):
    if lis2[i] in lis:
        lis.remove(lis2[i])
print(*lis)