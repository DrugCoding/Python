a = int(input())
for i in range(1, a +1):
    b = input()
    if b == b[::1]:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')
