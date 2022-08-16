a = int(input())

for _ in range(a):
    word = list(input().split())
    for i in word:
        print(i[::-1], end = ' ')