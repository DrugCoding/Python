N = input()
 
find = False
 
for i in range(2**len(N)):
    answer = ''
    for j in range(len(N)):
        if (i//(2**j)) % 2 == 0:
            answer += '7'+answer
        else:
            answer += '4'+answer
 
    if int(answer) <= int(N):
        find = True
        break
 
if not find:
    answer = ''
    for i in range(len(N)-1):
        answer += '7'
 
print(answer)


# 참고코드
# find = False 이해하기
# 