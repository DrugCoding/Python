N = int(input())

A = []
for i in range(N) : 
    A.append(int(input()))

one_count = A.count(1)
zero_count = A.count(0)

if one_count > zero_count :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")