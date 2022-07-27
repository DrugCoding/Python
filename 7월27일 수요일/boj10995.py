a = int(input())

if a == 1:
    print('*')

else:
    for i in range(1, a + 1):
        if i % 2 == 1:
            print('* ' * a)
        else:
            print(' *' * a)