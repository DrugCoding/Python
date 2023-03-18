word = input()
lis = []
lis.append(word)
for i in range(len(word)-1):
    lis.append(word[i+1:])
lis.sort()
for j in lis:
    print(j)
    