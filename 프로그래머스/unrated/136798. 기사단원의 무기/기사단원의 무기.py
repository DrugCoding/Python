from collections import deque

def solution(number, limit, power):
    st = deque([i for i in range(1,number+1)])
    divisor = []
    while st:
        count =0
        now = st.popleft()
        for i in range(1,int(now**0.5)+1):
            if now % i ==0:
                count +=1
                if i ** 2 != now:
                    count +=1
        divisor.append(count)
    return sum([power if i >limit else i for i in divisor])