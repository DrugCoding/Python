state = input()
stack = []
while state != '고무오리 디버깅 끝':
    if state == '문제':
        stack.append(state)
    elif state == '고무오리':
        # 문제가 있으면 풀기
        if stack:
            stack.pop()
        # 문제가 없으면 2문제 추가
        else:
            stack.append('문제')
            stack.append('문제')
    print(stack)
    state = input()

# 문제 남았으면
if stack:
    print("힝구")
else:
    print("고무오리야 사랑해")