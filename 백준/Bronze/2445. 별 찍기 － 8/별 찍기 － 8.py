a = int(input())

for i in range(1, a+1):
    print('*'*i+' '*(a-i)*2+'*'*i)
    
for i in range(1, a, 1):
    print('*'*(a-i)+' '*(i*2)+'*'*(a-i))