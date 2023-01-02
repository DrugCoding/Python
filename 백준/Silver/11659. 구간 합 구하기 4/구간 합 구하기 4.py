import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    sum_value = 0
    prefix_sum = [0]

    for y in arr:
        sum_value += y
        prefix_sum.append(sum_value)
    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        print(prefix_sum[j] - prefix_sum[i - 1])