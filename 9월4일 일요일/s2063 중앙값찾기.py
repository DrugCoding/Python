n = int(input())
lis = list(map(int,input().split()))
lis.sort()
print(lis[n//2])