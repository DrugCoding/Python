S, A = map(int, input().split())

max_ = []
max_.append(S // 2)
max_.append(A // 2)

print(min(max_))
