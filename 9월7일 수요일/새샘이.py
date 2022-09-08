lis = list(map(int, input().split()))
lis.sort()
lis.reverse()
lis2 = []
for i in range(2, 7):
    lis2.append(lis[0] + lis[1] + lis[i])
for i in range(3, 7):
    lis2.append(lis[0] + lis[2] + lis[i])
dic = set(lis2)
lis3 = [k for k, v in dic.items()]
lis3.sort()
lis3.reverse()
print(lis3)