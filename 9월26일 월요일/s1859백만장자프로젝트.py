n = int(input())

for i in range(1, n+1):
    m = int(input())
    lis = list(map(int, input().split()))

    max_ = lis[-1]
    profit = 0

    for j in range(m-2, -1, -1):
        if lis[j] >= max_:
            max_ = lis[j]
        else:
            profit += max_ - lis[j]
    
    print(f'#{i} {profit}')