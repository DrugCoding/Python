import sys
input = sys.stdin.readline

n= int(input().rstrip())
v = []
for i in range(n) :
  x, y = map(int, input().rstrip().split())
  v.append((x,y))

v.sort()

for x,y in v :
  print(x,y)