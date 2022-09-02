n, m = map(int, input().split())
cnt = 0
while True:
    if m == n:
        break
    else:  
        m += 1
        cnt += 1
print(cnt+1)
        