a = int(input())
for i in range(a):
    lis = list(map(int, input().split()))
    lis.sort()
    lis.reverse()
    print(lis[2])