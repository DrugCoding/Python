S = []
SS = []

for i in range(7):
    S.append(int(input()))

    if S[i] % 2 == 1:
        SS.append(S[i])

if len(SS) == 0:
    print("-1")
    
else :
    print(round(sum(SS)))
    print(min(SS))
                
