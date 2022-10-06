t = int(input())
for _ in range(t):
    lis = []
    a, b = map(str, input().split())
    a = int(a)
    for i in b:
        lis.append(i * a)
    print(*lis, sep='')