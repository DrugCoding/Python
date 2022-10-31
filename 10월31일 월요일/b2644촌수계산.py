n = int(input())
start, end = map(int, input().split())
m = int(input())
mat = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    mat[x].append(y)
    mat[y].append(x)
    
visited = [False] * (n + 1)

stack = []
visited[start] = True
stack.append((start, 0))

answer = -1

while len(stack) != 0:
    number, count = stack.pop()
    if number == end:
        answer = count
        break
    
    mat2 = mat[number]
    
    for mat3 in mat2:
        if not visited[mat3]:
            stack.append((mat3, count + 1))
            visited[mat3] = True
            
print(answer)