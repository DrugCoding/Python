n = int(input())
lis = list(map(int,input().split()))
	
lis2 = []
cnt = 0
for i in range(n-1):
    if lis[i+1] > lis[i]:
        cnt += lis[i+1] - lis[i]
    elif lis[i+1] <= lis[i]:
        lis2.append(cnt)
        cnt = 0
lis2.append(cnt)

if not lis2:
    print(0)
else:
    print(max(lis2))

# cnt 카운트 끝나는 시점에 것은 추가 되지 않기에 반복문 끝나고 추가 해주기.
# 리스트가 비어있음을 확인하는 not 문 