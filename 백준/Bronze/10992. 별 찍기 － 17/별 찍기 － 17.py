a = int(input())

for i in range(1, a+1):
    if i == 1 or i == a:
        print(' ' * (a-i), '*' * (2*i-1), sep='')
    else:
        print(' ' * (a-i), '*', ' ' * ((i-1) * 2 -1), '*', sep='')