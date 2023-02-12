sum_ = []
for i in range(10):
    a = int(input())
    sum_.append(a)

namugi = []
for i in sum_:
    if (i % 42) not in namugi: 
        namugi.append(i % 42)
    
print(len(namugi))