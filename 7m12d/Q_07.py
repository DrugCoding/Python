numbers = [0, 20, 100, 50, -60, 50, 100]

k = 0

for i in numbers:
    k = int(i)
    if k <= int(i+1):
        k = k
    else:
        k = int(i+1)

print(k)