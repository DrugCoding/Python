# 문제 09. 득표수 구하기

# Input

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

young = 0

for student in students:
    if student == '이영희':
        young += 1

print(young)