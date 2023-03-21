import sys
inStr, word = sys.stdin.read(), [0 for i in range(26)]
for s in inStr:
    if s.islower(): #소문자인지 체크
        word[ord(s)-97] += 1    # 알파벳을 아스키코드로 변환
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end='')    #아스키코드에 해당되는 문자로 변환