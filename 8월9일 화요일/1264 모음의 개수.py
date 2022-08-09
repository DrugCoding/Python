while True:
    a = input()
    if a == '#':
        break
    cnt = 0
    for i in a:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)