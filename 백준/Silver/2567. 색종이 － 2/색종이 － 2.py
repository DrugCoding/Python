from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
board = [[0] * 101 for _ in range(101)]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            board[i][j] = 1 # 색칠된 공간을 1로 바꾼다.
            
res = 0
for i in range(1, 101):
    for j in range(1, 101):
        if board[i][j] == 1: # 만약 1이면 (색칠이 되어있으면 cnt = 0)
            cnt = 0
            
            for k in range(4): #i, j 이동하는 것에 따라서 4방향 확인
                nx = i + dx[k] 
                ny = j + dy[k]
                
                if board[nx][ny] == 1: # 이동한 board가 색칠이 되어 있으면 색칠을 한다.
                    cnt += 1
                
            if cnt == 3: # cnt가 3이면 변이 하나기 때문에 res += 1
                res += 1
            elif cnt == 2: # cnt가 2이면 변이 두개 res += 2
                res += 2

print(res)