import sys


while True:
    string = sys.stdin.readline().rstrip()
    stack = list()

    if string == '.':
        break

    for x in string:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(x)
                break
        elif x == '[':
            stack.append(x)
        elif x == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(x)
                break
    if stack:
        print('no')
    else:
        print('yes')