n = int(input())
word = list(input())
cnt = 1
for i in range(1, n):
    if word[i - 1] != word[i]:
        cnt += 1
print(cnt)