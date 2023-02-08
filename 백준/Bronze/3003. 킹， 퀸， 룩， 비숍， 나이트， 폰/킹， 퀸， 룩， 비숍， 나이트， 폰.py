king = [1, 1, 2, 2, 2, 8]
list_ = list(map(int, input().split()))

for i in range(len(king)):
    print(king[i] - list_[i] , end = ' ')