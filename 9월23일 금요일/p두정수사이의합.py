def solution(a, b):
    if a <= b :
        return sum(range(a, b+1))
    else :
        return sum(range(b, a+1))