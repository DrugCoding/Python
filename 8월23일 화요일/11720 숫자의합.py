n = int(input())
word = input()

cnt = 0
for i in range(n):
    cnt += int(word[i])
    
print(cnt)