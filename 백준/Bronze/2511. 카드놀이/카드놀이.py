# a,b 에 input 값 넣기
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# A,B에 이긴 점수 / winner = 마지막 이긴 사람
x = 0
y = 0
winner = 0
# 10번 반복 a가 크면 x + 3 위너를 A로 변경
for i in range(10):
    if a[i] > b[i]:
        x += 3
        winner = 'A'
    elif a[i] < b[i]:
        y += 3
        winner = 'B'
    elif a[i] == b[i]:
        x += 1
        y += 1
# 만약 x가 크다면 프린트 x, y 점수 그리고 프린트 A
if x > y:
    print(x, y)
    print('A')
elif x < y:
    print(x, y)
    print('B')
# 만약 x y 가 같다면 마지막 위너로 비교
elif x == y:
    if winner == 'A':
        print(x, y)
        print('A')
    elif winner == 'B':
        print(x, y)
        print('B')
    else:
        print(x, y)
        print('D')