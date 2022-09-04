n = int(input())
for i in range(1, n+1):
    lis = list(map(int, input().split()))
    num = 0
    for j in lis:
        if j % 2 != 0:
            num += j
    print(f'#{i} {num}')