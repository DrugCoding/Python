a, b, c = map(int, input().split())
lis = [a, b, c]
dic = {}
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
if lis[0] == lis[1] == lis[2]:
    print(lis[0] * 1000 + 10000)
elif lis[0] == lis[1] or lis[0] == lis[2] or lis[1] == lis[2]:
    lis2 = [k for k, v in dic.items() if v == 2]
    print(lis2[0] * 100 + 1000)
else:
    print(max(lis) * 100)