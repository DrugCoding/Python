import sys

t = int(input())
lis = [int(sys.stdin.readline()) for _ in range(t)]

# t = int(input())
# num = []
# for _ in range(n):
#     num.append(int(sys.stdin.readline()))

lis.sort()
for i in lis:
    print(i)