a = int(input())

S = list(map(int, input().split()))

x = 0

for i in range(len(S)):
    if S[i] != i + 1:
        x += 1

print(x)