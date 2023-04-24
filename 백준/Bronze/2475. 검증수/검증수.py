star = list(map(int, input().split()))

ur = 0

for i in star:
    ur += i ** 2
    
print(ur % 10)