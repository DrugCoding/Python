def solution(s):
    answer = ''
    lis = list(s)
    lis.sort()
    lis = lis[::-1]
    for i in lis:
        if i.isupper == False:
            lis.pop(i)
            lis.append(i)
    for i in lis:
        answer += i
    return answer