num = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
a = input().lower()

cnt = 0
for i in range(len(a)):
    for j in num:
        if a[i] in j:
            cnt += num.index(j) + 3
print(cnt)