def solution(price, money, count):
    price2 = 0
    for i in range(1, count+1):
        price2 += price * i
    if price2 <= money:
        return 0
    else:
        return price2 - money