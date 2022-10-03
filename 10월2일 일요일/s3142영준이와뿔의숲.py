n = int(input())
for i in range(1, n + 1) :
    a, b = map(int, input().split())
    t = a - b 
    u = b - t
    
    print(f'#{i} {u} {t}')