# 15. 문자의 위치 구하기 (처음으로)
word = input()

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)