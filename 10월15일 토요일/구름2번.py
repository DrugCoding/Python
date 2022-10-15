a, b = input().split()
num = 0
for i in range(int(a)):
    word = input()
    if b in word:
        num += 1
print(num)