# input 값을 저장
a = int(input())
# card list를 만든다 # [1, 2, 3, 4, 5, 6, 7]
card = [i for i in range(1, a + 1)]
# 빈 버릴 카드를 담을 list 생성
fall = []

# 반복
while True:
    # fall에 추가(card list에 첫 번째 값) # [1] # [1, 3]
    fall.append(card.pop(0))
    # 만약 카드가 없다면 종료
    if not card:
        break
    # card 리스트의 첫 번째 값을 뽑아서 맨 뒤로 추가 # [3, 4, 5, 6, 7, 2] # [5, 6, 7, 4] 
    card.append(card.pop(0))

# 버린 카드 리스트 fall을 출력    
print(fall)