t = int(input())
lis = [int(input()) for _ in range(t)]
lis2 = []

for i in lis:
    if i != 0:
        lis2.append(i)
    elif i == 0:
        lis2.pop()
        
print(sum(lis2))