t = int(input())
for _ in range(t):
    cnt = 0
    avg = []
    lis = list(map(int, input().split()))
    n = [lis[0]]
    del lis[0]
    avg.append(sum(lis)/n[0])
    for i in lis:
        if i > avg[0]:
           cnt += 1
    score = cnt / n[0] * 100
    print(f'{score:.3f}%')
    # print(f'{round(cnt / n[0] * 100,3)}%')