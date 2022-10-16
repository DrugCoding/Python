n = int(input())
a = 100
b = 100
for _ in range(n):
    c, d = map(int, input().split())
    if c > d:
        b -= c
    elif c < d:
        a -= d
    elif c == d:
        pass
print(a)
print(b)