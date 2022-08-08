dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] # 다이얼 리스트 만들기
word = input() # input 값을 word에 넣기
time = 0 # 변수 time 생성

for i in range(len(word)): # word 길이만큼 반복
    for j in dial: # 다이얼리스트 반복
        if word[i] in j: # 만약 word의 첫 번째 자리가 다이얼리스트에 있다면
            time += dial.index(j) + 3 # time에 다이얼 인덱스 만큼 추가 하고 + 3(0부터 시작하기에 2가아닌 3)

print(time)