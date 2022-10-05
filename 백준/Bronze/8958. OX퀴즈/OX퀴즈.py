t = int(input())
for _ in range(t):
    word = input() 
    sum_ = 0
    num = 1
    for i in range(len(word)):
        if word[i] == 'O':
            sum_ += num
            num += 1
        else:
            num = 1
    print(sum_)