a = int(input())

for i in range(0, a):
    print(' '*i+'*'*(a-i)+'*'*(a-i-1))

for i in range(a, 1, -1):
    print(' '*(i-2)+'*'*(a-i+2)+'*'*(a-i+1))