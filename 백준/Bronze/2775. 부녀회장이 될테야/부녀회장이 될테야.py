n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())
    lis = [i for i in range(1, b + 1)]
    
    for j in range(a):
        for k in range(1, b):
            lis[k] += lis[k - 1]
    print(lis[-1])