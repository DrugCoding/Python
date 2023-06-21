word = input()
words = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in words:
    word = word.replace(i, 'A')
print(len(word))