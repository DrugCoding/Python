a = int(input())


if a == 1:
    print('*')
    
else :
    for i in range(a):
        if i % 2 == 0:
            print('* '*a)
        else:
            print(' *'*a)