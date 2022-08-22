n = int(input())
lis = list(map(int, input().split()))
m = int(input())
dic = {}
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
  
if m not in dic:
    print(0)
else:
    print(dic.get(m))