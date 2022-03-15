# ex01.py
# 리스트 관리 프로그램에서 함수 활용하기



def showMenu():         # 매개변수도 전달받지 않고, 반환값도 없다
    print('1. 목록')
    print('2. 추가')
    print('3. 검색')
    print('4. 삭제')
    print('0. 종료')

def showList(memberList):               # 매개변수는 있고, 반환값음 없음
    print('{:=^25}'.format('멤버 목록'))
    for mem in memberList:
        print('-', mem)
    print()

def searchFromList(search, memberList): # 매개변수도 있고 반환값도 있음
    for mem in memberList:      #memberList 안의 각각의 요소에 대해서
        if search in mem:       # 검색어가 포함되어 있다면
            return mem          # 해달 멤버를 반환 (함수 호출 자리로 이동)
    return None                 # 반복문이 끝나도 원하는 값을 찾지 못했다면 None 반환
    # 없음, null과 유사하게 사용

def deldteFromList(search, memberList):
    for mem in memberList:
        if search == mem:       # 검색어와 일치하는 멤버가 있다면  
            memberList.remove(mem)
            return 1            # 삭제된 객체 수를 반환(삭제되었음)
    return 0                # 삭제된 객체 수를 반환(삭제된 내용이 없음)

memberList = ['원종래', '구승현', '이지은']

while True:
    showMenu()
    menu = input('입렵 >>>')

    if menu == '1':
        showList(memberList)

    if menu == '2':
        memberList.append(input('추가할 멤버 입력 : '))

    if menu == '3':
        result = searchFromList(input('검색할 이름 입력 : '), memberList)
        print(result != None and result or '검색 결과가 없습니다')

    if menu == '4':
        result = deldteFromList(input('삭제할 이름 입력 : '), memberList)
        print(result == 1 and '삭제되었습니다' or '대상을 찾을 수 없습니다')


    if menu == '0':
        break

   
    print()
print('프로그램 종료')
