def solution(number):
    answer = 0
    for a in range(len(number)):
        for b in range(a + 1, len(number)):
            for c in range(b + 1, len(number)):
                if number[a] + number[b] + number[c] == 0:
                    answer += 1
    return answer