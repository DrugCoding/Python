# a, b = map(int, input().split())
# no1 = [input() for _ in range(a)]
# no2 = [input() for _ in range(b)]

# noman = []
# for i in no1:
#     if i in no2:
#         noman.append(i)
        
# noman.sort()
# print(len(noman))
# for j in noman:
#     print(j)
----------------------------------------
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = dict()
answer = []
for i in range(n):
    x = input()
    if x not in arr1:
        arr1[x] = i

for i in range(m):
    y = input()
    if y in arr1:
        answer.append(y)
        
answer.sort()
print(len(answer))
print(''.join(answer), end = '')