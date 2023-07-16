while True:
    n = int(input())
    if n == 0:
        break
    else:
        lis = []
        for _ in range(n):
            word = input()
            lis.append(word)
        lis.sort(key=str.lower)
        
        print(lis[0])