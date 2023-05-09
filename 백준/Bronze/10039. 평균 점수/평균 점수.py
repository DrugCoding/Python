score_list = []

for i in range(5):
    
    score = int(input())
    
    if score < 40:
        score_list.append(40)
    else:
        score_list.append(score)
        
print(round(sum(score_list)/5))