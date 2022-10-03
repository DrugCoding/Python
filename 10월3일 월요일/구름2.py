n, m = map(str, input().split())
lis = []
for _ in range(int(n)):
	lis.append(input())

cnt = 0	
for j in lis:
	if m in j:
		cnt += 1
		
print(cnt)

# 동명이인