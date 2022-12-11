import sys
input = sys.stdin.readline

a, b, c = -1, 0, 0
for i in range(9):
    arr = list(map(int,input().split()))
    for j in range(9):
        if arr[j] > a:
            a, b, c = arr[j],i,j
print(a, b + 1, c + 1,sep = "\n")