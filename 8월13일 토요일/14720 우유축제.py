a = int(input())
lis = list(map(int, input().split()))
cnt = 0
for i in lis:
    if i == cnt % 3:
        cnt += 1
print(cnt)