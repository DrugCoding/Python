n = int(input())
for i in range(1, n+1):
    lis = list(map(int, input().split()))
    lis.sort()
    print(f'#{i} {lis[0] + lis[5] + lis[6]}')