word = input()
lis = list(word)
lis.sort(reverse=True)
print(*lis, sep='')