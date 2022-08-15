a = int(input())
lis = []
for i in range(a+a-1):
    lis.append(input())
dic = {}
for i in lis:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
key_ = list(dic.keys())
value_ = list(dic.values())
s = value_.index(1)
print(key_[s])

# stdin.readline() 사용시 시간초과 안남
# n = int(stdin.readline())
# m = {}

# # 참가자 이름
# for i in range(n):
#     name = stdin.readline()
#     if name in m :
#         m[name] += 1
#     else :
#         m[name] = 1

# # 완주자 이름 
# for i in range(n-1):
#     name = stdin.readline()
#     if m[name] == 1 :
#         del m[name]
#     elif name in m :
#         m[name] -= 1
        
# print(*m)