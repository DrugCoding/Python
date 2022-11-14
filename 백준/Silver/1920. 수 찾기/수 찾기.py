import sys

n = int(sys.stdin.readline())
N = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

for i in M:
    if i in N:
        print(1)
    else:
        print(0)