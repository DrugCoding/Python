dust = int(input('숫자를 입력하시오'))

if dust >150:
    if dust > 300:
        print('실외활동을 자제하세요')
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust < 0:
        print('음수')
    else:
        print('좋음')