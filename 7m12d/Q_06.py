numbers = [0, 20, 90, 50, -60, 50, 80]

k = numbers[0]

for i in numbers:
    if k > i:
        k = k
    else:
        k = i
print(k)