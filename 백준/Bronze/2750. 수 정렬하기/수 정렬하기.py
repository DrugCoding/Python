a = int(input())

list_ = []

for i in range(a):
    list_.append(int(input()))
new_list = sorted(list_)

for i in range(a):
    print(new_list[i])