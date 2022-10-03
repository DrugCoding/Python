lis = list(map(int, input().split()))
lis.sort()
lis2 = []
lis2.append(lis[0] + lis[1])
lis2.append(lis[2] + lis[3])
print(lis2[1] - lis2[0])
# 최장 맨해튼 거리