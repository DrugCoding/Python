a = list(map(int, input().split()))
b = []
for i in range(1, 9):
    b.append(i)
if a == b:
    print('ascending')
elif a == b[::-1]:
    print('descending')
else:
    print('mixed')