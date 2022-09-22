def solution(n):
    lis = list(str(n))
    lis.sort()
    lis.reverse()
    lis = ''.join(lis)
    return int(lis)