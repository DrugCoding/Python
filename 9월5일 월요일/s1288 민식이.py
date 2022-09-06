T = int(input())
for t in range(1, T + 1):
    num = int(input())
 
    arr = [False]*10
    j = 1
    cnt = 0
    while cnt != 10:
        sleep = str(num*j)
        for i in sleep:
            if arr[int(i)] == False:
                arr[int(i)] = True
                cnt += 1
        j += 1
    print("#{} {}".format(t, num*(j-1)))
    #재도전하기