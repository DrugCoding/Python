s = int(input())
for _ in range(s):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    print(box)
    cnt = 0
    for i in range(m): # 4
        for j in reversed(range(n)): # 5 / 0 ~ 4
            if box[j][i] == 1:
                while True:
                    if j + 1 == n:
                        break
                    if box[j+1][i] == 1:
                        break
                    box[j][i] = 0
                    box[j+1][i] = 1
                    j += 1
                    cnt += 1
    print(cnt)