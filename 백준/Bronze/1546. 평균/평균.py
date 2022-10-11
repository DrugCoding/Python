t = int(input())
lis = list(map(int, input().split()))

max_ = max(lis)
lis2 = []

for i in lis :
    lis2.append(i/max_ * 100)
avg = sum(lis2)/t

print(avg)