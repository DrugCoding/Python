text = []
for i in range(5):
    text.append(input())
for i in range(max(len(e) for e in text)):
    for j in range(5):
        if i < len(text[j]):
            print(text[j][i], end='')