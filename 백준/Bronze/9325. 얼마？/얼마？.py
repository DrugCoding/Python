num = int(input())
for _ in range(num):
    money = int(input())
    n = int(input())
    sum_ = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum_ += a * b
    print(sum_ + money)