n = int(input())
for i in range(1, n+1):
    lis = list(map(int, input().split()))
    print(f'#{i} {max(lis)}')