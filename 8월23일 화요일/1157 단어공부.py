word = input()
word = word.upper()

dic = {}
for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

lis = [v for k, v in dic.items()]

if lis.count(max(lis)) == 1:
    for k, v in dic.items():
        if v == max(lis):
            print(k)
else:
    print('?')