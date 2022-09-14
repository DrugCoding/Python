n = int(input())
for _ in range(n):
    m = int(input())
    lis = list(map(int, input().split()))
    dic = {}
    for i in lis:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    # print(dic)
    lis2 = [v for k, v in dic.items()]
    # print(lis2)
    lis3 = [k for k, v in dic.items() if v == max(lis2)]
    # print(lis3)
    if len(lis3) == 1:
        print(f'#{m} {lis3[0]}')
    else:
        print(f'#{m} {max(lis3)}')