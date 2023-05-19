a = int(input())

li = list(map(int, input().split()))

sum = 0
res = 0

for i in range(a):
    if li[i] == 1:
        sum += 1
        res += sum
    else:
        sum = 0
        
print(res)