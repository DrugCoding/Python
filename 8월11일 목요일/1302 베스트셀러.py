a = int(input())
dic = {}
for i in range(a):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

value_ = []
for j in dic:
    value_.append(dic[j])

max_ = max(value_)

key_ = []
for k, v in dic.items():
    if v == max_:
        key_.append(k)

key_.sort()
print(key_[0])