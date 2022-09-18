def sol(a):
    answer = 0
    for i in range(1, a + 1):
        if a % i == 0:
            answer += i
    return answer

print(sol(12))