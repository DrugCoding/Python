import sys
sys.stdin = ('행복한지.txt', 'r')

word = input()

happy = []
sad = []

happy.append(word.count(':-)'))
sad.append(word.count(':-('))

if happy[0] == 0 and sad[0] == 0:
    print('none')
elif happy[0] == sad[0]:
    print('unsure')
elif happy[0] > sad[0]:
    print('happy')
else:
    print('sad')