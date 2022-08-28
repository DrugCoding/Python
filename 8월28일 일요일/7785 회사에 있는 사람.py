# 1번 풀이 (백준 실패)
n = int(input())
dic = {}
for _ in range(n):
    a, b = input().split()
    if a in dic:
        dic[a] = 'leave'
    else:
        dic[a] = 'enter'

lis = []
for k, v in dic.items():
    if v == 'enter':
        lis.append(k)
lis.sort(reverse=True)

print(*lis, sep = '\n')

# 2번 풀이 (백준 통과)
n = int(input())
dic = {}
for _ in range(n):
    a, b = input().split()
    dic[a] = b
    
lis = []
for k, v in dic.items():
    if v == 'enter':
        lis.append(k)

lis.sort()
lis.reverse()
print(*lis, sep = '\n')