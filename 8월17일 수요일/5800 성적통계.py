import sys
sys.stdin = ('성적통계.txt','r')

n = int(input())

for j in range(n):
    lis = list(map(int, input().split()))
    lis.remove(lis[0])
    # print(lis)
    lis.sort()
    # print(lis)
    print(f'Class {j+1}')
    
    lis2 = []
    for i in range(len(lis)-1):
        lis2.append(lis[i+1] - lis[i])
    # print(lis2)
    print(f'Max {max(lis)}, Min {min(lis)}, Largest gap {max(lis2)}')