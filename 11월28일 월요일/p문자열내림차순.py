def solution(s):
    answer = ''
    lis = list(s)
    lis.sort()
    lis = lis[::-1]
    for i in lis:
        if i.isupper() == 'True':
            lis.pop(i)
            lis.append(i)
    for i in lis:
        answer += i
    return answer

# "문자열".isupper() 시 해당 문자열이 대문자면 'True' 아니면 'False' 반환