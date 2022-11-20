def solution(n):
    answer = ''
    if n % 2 == 0:
        for _ in range(n//2):
            answer += '수박'
    else:
        for _ in range(n//2):
            answer += '수박'
        answer += '수'
    
    return answer