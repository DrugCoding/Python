people_in = [0]

for i in range(4):
    _out, _in = map(int, input().split())
    people_in.append(people_in[-1] - _out + _in)
    
    people_in
    
print(max(people_in))