a = input()
for i in range(int(a)):
    num, word = map(str, input().split())
    word = word[:int(num) - 1] + word[int(num):]
    print(word)