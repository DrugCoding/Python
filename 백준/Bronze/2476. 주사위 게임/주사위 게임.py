n = int(input())
data = []

for _ in range(n) :
  a, b, c = map(int, input().split())
  if a == b == c :
    data.append(10000 + a * 1000)
  elif a == b :
    data.append(1000 + a * 100)
  elif a == c :
    data.append(1000 + a * 100)
  elif b == c :
    data.append(1000 + b * 100)
  else :
    data.append(max(a, b, c) * 100)

print(max(data))