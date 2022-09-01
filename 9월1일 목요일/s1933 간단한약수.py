n = int(input())
for i in range(N):
    if n % (i+1) == 0:
        print(i+1, end=" ")