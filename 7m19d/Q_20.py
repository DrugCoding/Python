from re import S


number = 123
result = 0
while number:
    result += number%10
    number //= 10
    # number, remainder= divmod(number, 10)
    # result += remainder
print(result)