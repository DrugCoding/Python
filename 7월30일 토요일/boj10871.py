a, b = map(int, input().split())

list_ = list(map(int, input().split()))

for i in range(a):
    if  list_[i] < b:
        print(list_[i], end = ' ')