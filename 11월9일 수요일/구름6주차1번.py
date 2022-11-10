for _ in range(5):
    word = input()
    a = 0
    for i in range(7):
        if i % 2 == 0:
            a += int(word[i])

    for k in range(7):
        if k % 2 != 0 and int(word[k]) != 0:
            a = a * int(word[k])
            
    print(a % 10)
