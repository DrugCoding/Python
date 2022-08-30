n, m = map(int, input().split())
if n == 3 and m == 1:
    print('B')
elif n == 3 and m == 2:
    print('A')
elif n == 2 and m == 1:
    print('A')
elif n == 2 and m == 3:
    print('B')
elif n == 1 and m == 2:
    print('B')
elif n == 1 and m == 3:
    print('A')