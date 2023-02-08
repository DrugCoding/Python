n, m = map(int, input().split())
if m < 45:
    m = m + 60 - 45
    if n == 0:
        n = 24
        n -= 1
    else:
        n -= 1
else:
    m -= 45
print(f'{n} {m}')