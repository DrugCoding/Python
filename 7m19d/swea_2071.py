a = int(input())

for i in range(1, a + 1):
    li = list(map(int, input().split()))
    av = sum(li) / len(li)
    av = round(av)
    print(av)