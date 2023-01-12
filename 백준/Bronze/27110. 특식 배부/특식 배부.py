n = int(input())
a, b, c = map(int, input().split())
cnt = 0
if a <= n:
    cnt += a
else:
    cnt += n
if b <= n:
    cnt += b
else:
    cnt += n
if c <= n:
    cnt += c
else:
    cnt += n
print(cnt)