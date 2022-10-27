import sys
input = sys.stdin.readline

n = int(input())
dic = {
    1 : "1.,?!",
    2 : "2ABC",
    3 : "3DEF",
    4 : "4GHI",
    5 : "5JKL",
    6 : "6MNO",
    7 : "7PQRS",
    8 : "8TUV",
    9 : "9WXYZ",
}
command = input()
ans = ''
cnt = 0
for i in range(n):
    if i == n:
        break
    else:
        if command[i+1] == command[i]:
            cnt += 1
            continue
        else:
            cnt %= len(dic[int(command[i])])
            ans += dic[int(command[i])][cnt]
            cnt = 0
print(ans)