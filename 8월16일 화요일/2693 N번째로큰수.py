a = int(input())
for i in range(a):
    lis = list(map(int, input().split()))
    lis.sort(reverse=True)
    print(lis[2])