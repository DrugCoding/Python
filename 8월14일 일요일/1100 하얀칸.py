matrix = [list(input()) for _ in range(8)]

cnt = 0
for x in range(8):
    for y in range(8):
        if (x + y) % 2 == 0 and matrix[x][y] == 'F':
            cnt += 1
            
print(cnt)