n = int(input())
lis = list(map(int, input().split()))
m = int(input())
lis2 = list(map(int, input().split()))
dic = {}
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
lis3 = []
for i in lis2:
    if i in dic:
        lis3.append(dic.get(i))
    else:
        lis3.append(0)
print(*lis3)