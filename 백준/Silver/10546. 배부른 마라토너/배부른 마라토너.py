from sys import stdin

n = int(stdin.readline())
m = {}

# 참가자 이름
for i in range(n):
    name = stdin.readline()
    if name in m :
        m[name] += 1
    else :
        m[name] = 1

# 완주자 이름 
for i in range(n-1):
    name = stdin.readline()
    if m[name] == 1 :
        del m[name]
    elif name in m :
        m[name] -= 1
        
print(*m)