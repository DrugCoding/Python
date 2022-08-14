word = 'banana'


result = {}

for char in word:
    # 딕셔너리에 키가 있으면?
    if not char in result:
        result[char] = 1
    # 딕셔너리에 키가 없으면?
    else:
        result[char] = result[char] + 1
print(result)