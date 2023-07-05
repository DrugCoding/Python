lis = list(map(str, input().split()))

min_ = []
max_ = []
for i in range(2):
    if '5' in lis[i]:
        max_.append(lis[i].replace('5', '6'))
    else:
        max_.append(lis[i])
        
for i in range(2):
    if '6' in lis[i]:
        min_.append(lis[i].replace('6', '5'))
    else:
        min_.append(lis[i])
        
print(sum(map(int, min_)), sum(map(int, max_)))