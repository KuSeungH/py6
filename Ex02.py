# ex02.py
# 파이썬에서 기본으로 제공하는 함수들

# 1) 문자열 관련 함수

str1 = 'Hello Python World'

print("str1.count('o') :", str1.count('o'))
# 매개변수로 전달하는 글자가 총 몇개나 있는지 정수로 변환

print("str1.find('o') :", str1.find('o'))
# 문자열 인덱싱 기준으로
# 매개변수 글자가 몇번째 위치에 있는지 정수로 변환

print("':'.join(str1) :", ':'.join(str1))
# 매개변수 문자열을 지정한 글자로 연결하여 반환

print("str1.upper() :", str1.upper())
# 문자열을 대문자 형식으로 변경하여 반환

print("str1.lower() :", str1.lower())
# 문자열을 소문자 형식으로 변경하여 반환

print("str1.lstrip() : [{}]".format(str1.lstrip()) )
# 왼쪽의 공백을 제거한다.
# 특정 글자를 매개변수로 전달하면 그 글자를 제거한다
# 반복해서 나타난다면 글자가 없을때 까지 제거 한다

print("str1.rstrip() : [{}]".format(str1.rstrip()) )
# 오른쪽 공백(혹은 매개변수 글자)을 제거 한다

print("str1.strip() : [{}]".format(str1.strip()) )
# 양쪽 공백(혹은 매개변수 글자)을 제거 한다

print("str1.replace() : ", str1.replace('Hello', 'Hi'))
# replace(A, B): A를 찾아서 B로 바꾼 문자열 반환

print("str1.split() : ", str1.split())
# 공백(혹은 매개변수 글자)를 기준으로 분리하여
# 리스트 형식으로 반환한다

print("str1.split(o) : ", str1.split('o'))


options = '바닐라시럽,카라멜시럽,헤이즐넛시럽,샷추가'
optionList = options.split(',')
for option in optionList:
    print(option)
print()

cardNumber = '1234-5678-1234-5678'
numnerList = cardNumber.split('-')
print(numnerList)
print()

query ='where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=이지은'
query1 = query.split('&')
queryList = []

print(query1)
for q in query1:
    key = q.split('=')[0]
    value = q.split('=')[1]
    param = {}
    param[key] = value
    queryList.apppd(param)

print(queryList)