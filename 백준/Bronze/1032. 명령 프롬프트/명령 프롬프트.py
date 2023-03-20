n = int(input())
b = []

for i in range(n):
    b.append(input())

c = list(b[0])

for i in range(n):
    for a in range(len(c)):
        if c[a] == b[i][a]:
            continue
        else:
            c[a] = '?'

print(''.join(c))