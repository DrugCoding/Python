a = int(input())
print(' '*(a-1) + '*')
for i in range(a-1):
    print(' '*(a-2-i) + '*' + ' '*(2*i+1) + '*')