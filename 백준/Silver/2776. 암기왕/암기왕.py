a = int(input())
for _ in range(a):
    b = int(input())
    lis1 = set(map(int, input().split()))
    c = int(input())
    lis2 = list(map(int, input().split()))
    
    for i in lis2:
        if i in lis1:
            print(1)
        else:
            print(0)