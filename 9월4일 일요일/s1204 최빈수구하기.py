n = int(input())
for _ in range(n):
    j = int(input())
    lis = list(map(int, input().split()))
    dic = {}
    for i in lis:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    lis2 = []
    val = [v for k, v in dic.items()]
    for k, v in dic.items():
        if v == max(val):
            lis2.append(k)
    if len(lis2) == 1:
        print(f'#{j} {lis2[0]}')
    else:
        print(f'#{j} {max(lis2)}')