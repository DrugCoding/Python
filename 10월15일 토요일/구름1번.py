n = int(input())
lis = list(map(int, input().split()))
num = lis[0]
del lis[0] 
for i in range(n - 1):
    num *= lis[i]
print(num)
