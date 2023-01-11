n = int(input())
han = 99

if n < 100:
    han = n
else:
    for i in range(100, n+1):
        a = list(map(int, str(i)))
        if a[0]-a[1] == a[1]-a[2]:
            han += 1

print(han)