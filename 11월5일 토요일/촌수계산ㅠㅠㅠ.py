n = int(input())
start, end = map(int, input().split())
m = int(input())
mat = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    mat[x].append(y)
    mat[y].append(x)

visited = [False] * (n + 1)

stack = []
stack.append((start, 0))
visited[start] = True

answer = -1

while len(stack) != 0:
    number, count = stack.pop()
    if number == end:
        answer = count
        break
    
    adj_graph = mat[number]
    
    for adj_number in adj_graph:
        # 방문한적이 없을 때만 스택에 값을 append
        if not visited[adj_number]:
            # 인접 번호와 촌수 + 1를 같이 append
            stack.append((adj_number, count + 1))
            # 인접 값을 방문 표시
            visited[adj_number] = True
            
# 그래서 촌수는 어떻게 계산을 해야될까?
# 촌수 출력
print(answer)