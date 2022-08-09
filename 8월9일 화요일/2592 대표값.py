import sys
sys.stdin = open('대표값.txt','r')

list_ = []
for i in range(10):
    list_.append(int(input()))
dic = {}
for j in list_:
    if j in dic:
        dic[j] += 1
    else:
        dic[j] = 1

max_ = max(dic.values())
max_key = []
for key, value in dic.items():
    if value == max_:
        max_key.append(key)

print(int(sum(list_)/10))
print(max_key[0])