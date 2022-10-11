t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    for i in range(n):
        a, b = input().split()
        dic[a] = int(b)
    lis = [v for k, v in dic.items()]
    lis2 = max(lis)
    print(*[k for k, v in dic.items() if v == lis2])
