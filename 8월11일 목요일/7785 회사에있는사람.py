a = int(input())
dic = {}
for i in range(a):
    k, v = input().split()
    dic[k] = v

lis = []
for k in dic:
    if dic[k] == 'enter':
        lis.append(k)

lis.sort(reverse=True)
for j in lis:
    print(j)