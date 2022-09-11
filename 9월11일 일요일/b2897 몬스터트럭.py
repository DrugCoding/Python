n, m = map(int, input().split())
lis = [list(input()) for _ in range(n)]
lis2 = [0] * 5

for i in range(n-1):
    for j in range(m-1):
        box = []
        box.append(lis[i][j])
        box.append(lis[i][j+1])
        box.append(lis[i+1][j])
        box.append(lis[i+1][j+1])
        
        if '#' not in box:
            car = box.count('X')
            if car == 0:
                lis2[0] += 1
            elif car == 1:
                lis2[1] += 1
            elif car == 2:
                lis2[2] += 1
            elif car == 3:
                lis2[3] += 1
            elif car == 4:
                lis2[4] += 1

for i in range(5):
    print(lis2[i])