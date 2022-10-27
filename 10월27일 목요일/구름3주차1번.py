t = int(input())
lis = list(map(int, input().split()))
dic = {}
for i in lis:
	dic[i] = 1
print(sum(dic.keys()))