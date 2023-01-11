# 실패코드(시간초과)
def solution(phone_book):
    answer = True
    phone_len = []
    for i in phone_book:
        phone_len.append(len(i))
        
    phone_min = []
    for k in phone_book:
        if len(k) == min(phone_len):
            phone_min.append(k)
            
    for a in phone_min:
        for b in phone_book:
            if a == b:
                continue

            if a == b[0:len(a)]:
                answer = False
                break
            
    return answer

# 성공코드
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break
    return answer