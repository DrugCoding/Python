n = int(input())
for _ in range(n):
    word = input()
    word2 = word[::-1]
    print(word[0], word2[0], sep='')