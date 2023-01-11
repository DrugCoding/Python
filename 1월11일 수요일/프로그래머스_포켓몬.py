def solution(nums):
    answer = 0
    setcount = len(list(set(nums)))
    liscount = len(nums) // 2
    if liscount == setcount:
        answer += setcount
    elif liscount > setcount:
        answer += setcount
    else:
        answer += liscount
    return answer