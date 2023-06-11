a = int(input()) # input 값 받기

matrix = [list(input()) for i in range(a)] # 메트릭스 받기

ans = [0, 0] # 답 넣을 곳
for i in range(a): # 5번 반복
    x, y = 0, 0 # x,y 가로 세로 = 0
    for j in range(a): # 5번 반복
        if matrix[i][j] == '.': # 위치에 . 가 있다면
            x += 1 # x 에 +1
        else: # 그게 아니라면 
            x = 0 # x 를 다시 0 으로
        if x == 2: # 
           ans[0] += 1 # 
        
            
        if matrix[j][i] == '.':
            y += 1
        else:
            y = 0
        if y == 2:
            ans[1] += 1
            
print(*ans)