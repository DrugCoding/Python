def solution(n):
    res = n**(1/2)
    
    if res % 1 == 0:
        return (res+1)**2
    else: return -1