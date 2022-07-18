word = "HappyHacking"

li = list(word)
count = 0

for i in li:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1

print(count)