n = int(input())
lis = list(map(int, input().split()))
main, sub = map(int, input().split())
m = 0
s = 0

for i in lis:
    i -= main
    m += 1
    s += i // sub
    # print(s)
    if i % sub == 0:
        continue
    else:
        s += 1

print(m + s)