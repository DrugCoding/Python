t = int(input())
for _ in range(t):
    a = int(input())
    lis = list(map(int, input().split()))
    avg = sum(lis) / a
    cnt = 0
    for i in lis:
        if i >= avg:
            cnt += 1
    print(cnt,'/',a, sep='')