def solution(participant, completion):
    answer = ''
    dic = {}
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in completion:
        if j in dic:
            dic[j] += 1
            
    lis = [k for k, v in dic.items() if v % 2 != 0]
    
    answer += lis[0]
        
    return answer