def solution(s):
    answer = True
    lower = s.lower()
    
    pcount = lower.count("p")
    ycount = lower.count("y")
    
    if pcount == ycount:
        answer = True
    elif pcount != ycount:
        answer = False

    return answer