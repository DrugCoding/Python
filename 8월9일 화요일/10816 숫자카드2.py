a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = list(map(int, input().split()))
e = []
for i in d:
    if i not in b:
        e.append(0)
    if i in b:
        e.append(b.count(i))
print(*e)