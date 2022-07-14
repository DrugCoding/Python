word = 'banana'

result = []

for idx in range(len(word)):
    if word[idx] == 'a':
        result.append(idx)

print(result)