a = int(input())
ball = [1, 0, 0]

for i in range(a):
    x, y = map(int, input().split())
    ball[x-1], ball[y-1] = ball[y-1], ball[x-1]
    
print(ball.index(1) + 1)
    