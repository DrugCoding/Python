sum1 = int(input())
t = int(input())
sum2 = 0
for _ in range(t):
    a, b = map(int, input().split())
    sum2 += (a * b)
if sum1 == sum2:
    print('Yes')
else:
    print('No')