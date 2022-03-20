# ex03.py
# 문자열 함수를 활용하여 카드번호 검증 알고리즘 구현해보기

'''
    신용카드는 총 16자리의 숫자로 구성되어 있다
    언뜻 보기에는 무작위 숫자처럼 보이지만 수학적 비밀이 하나 있다
    카드번호가 유호한지 검사하기 위한 Luhn 알고리즘이 있다

    1) 신용카드 16자리 숫자중에서 우측부터 세어서 홀수번째는 그대로 둔다
    2) 16자리 숫자중 우측부터 세어서 짝수번째는 2배로 만든다
    3) 2배로 만든 숫자가 10 이상이라면 각 자릿수를 합해서 한자리수로 만든다
    4) 이와같이 얻은 16개의 정수를 모두 더한다
    5) 모두 더한 값이 10으로 나누어 떨어지면 유호한 카드번호이다
    6) 모두 덜한 값이 10으로 나눈어 떨어지지 않으면 유호하지 않은 번호이다

    2720-9927-1182-8767      True
    3444-0639-1046-2763      False
    6011-7338-9510-6094      True
'''

def isValid(cardNumber):
    # 1) 입력받은 카드번호에서 -를 제거한다 (replace)
    cardNumber = cardNumber.replace('-','')
    cardNumber = cardNumber.replace(' ','')
    if len(cardNumber) != 16:       # -를 제거한 상태에서 16자리가 아니라면
        return False                # 이후 코드 진행할 필요 없이 False 반환
    print(cardNumber)
    total = 0

    # 2) 각 자릿수의 글자를 숫자형태로 변환하여 우축에서 짝수번째만 2배로 만들기
    for i in range(len(cardNumber)):
        num = int(cardNumber[i])
        if i % 2 == 0:
           num *= 2

            # 3) 2배된 수가 10보다 크면 각 자릿수를 더해서 결과값 만들기
           if num > 10:
               num = num // 10 + num % 10
        # print(num, end='')
        total += num
    print(total)

     # 4) 각 자릿수의 합계를 구하여 10으로 나누어 떨어지면 Ture, 아니면 False
    return total % 10 == 0     # Ture 혹은 False 를 반환

cardNumber = input('카드 번호 입력 (xxxx-xxxx-xxxx-xxxx) : ')

result = isValid(cardNumber)
if result:
    print(cardNumber, '는 유호한 카드번호 입니다')
else:
    print(cardNumber, '는 유효하지 않습니다')