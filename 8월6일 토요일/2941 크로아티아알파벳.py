word = input() # input 문자열
words = ['c=','c-','dz=','d-','lj','nj','s=','z='] # 크로아티아 문자열 리스트

for i in words: # 크로아티아 문자열 반복
    word = word.replace(i, 'A') # input문자열에 i가 있다면 A로 바꿔서 그것이 word
print(len(word)) # print word의 길이