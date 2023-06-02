coin = 1000 - int(input())
li = [500, 100, 50, 10, 5, 1]
count = 0

for i in li:
    count += coin // i
    coin = coin%i
    
print(count)