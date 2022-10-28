# def solution(arr):
#     answer = []
#     arr.remove(min(arr))
#     answer.append(arr)
#     if len(answer) > 1:
#         return sum(answer,[])
#     else:
#         return -1
    
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))

        return arr
    else:
        return [-1]