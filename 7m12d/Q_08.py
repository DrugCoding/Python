from tkinter import N


numbers = [0, 20, 100, 40]

max_namber = numbers[0]
seceond_number = numbers[0]

# 1. wjscp tntwkfmf qksqhr
for i in numbers:
    # 만약에, n이 최대보다 크다면
    if max_namber < n:
        # 최대값이 었던 것이 두번째로 큰 수
        seceond_number = max_namber
        max_namber = n
    elif seceond_number < n < max_namber:
        seceond_number = n
print(seceond_number)