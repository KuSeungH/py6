# quiz1.py
# 2021 KAKAO BLIND RECRUITMENT [신규 아이디 추천 Lv. 1]

'''
    신규 사용자에게 아이디를 추천합니다
    - 아이디의 길이는 3자 이상 15자 이하여야 합니다
    - 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다
    - 단, 마침표(.)는 처음과 끝에 사용할 수 없으며, 또한 연속으로 사용할 수 없습니다

    다음 7단계를 거쳐 신규유저가 입력한 아이디를 검사하여 규칙에 맞는 추천을 해줍니다
    신규 유저가 입력한 아이디가 new_id 라고 한다면ㅁ,

    1) new_id의 모든 대문자를 대응되는 소문자로 치환합니다
    2) new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한
       모든 문자를 제거합니다
    3) new_id에서 마침표(.)가 2번이상 연속된 부분을 하나의 마치표(.)로 치환합니다
    4) new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다
    5) new_id가 빈 문자열이라면, new_id에 "a" 를 대입합니다
    6) new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한
       나머지 문자들을 모두 제거합니다
       만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 마지막 마침표(.)를  제거합니다
    7) new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될때까지
       반복해서 끝에 붙입니다


    입출력 예시
    입력 : "...!@Bat#*..Y.abcdefghijklm"
    출력 : "bat.y.abcdefghi"

    입력 : "z-=.^."
    출력 : "z--"
    
    입력 : "=.="
    출력 : "aaa"

    입력 : "123_.def"
    출력 : "123_.def"

    입력 : "abcdefghijklmn.p"
    출력 : "abcdefghijklmn"

    lower(), for, in, nwe_id[i], strip(), len(nwe_id), while, replace
'''

def solution(nwe_id):
    # 1) new_id의 모든 대문자를 대응되는 소문자로 치환합니다
    # 함수의 내용을 완성하세요
    nwe_id = nwe_id.lower()

    # 2) new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다
    filter = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'
    answer = ''
    for ch in nwe_id:
        if ch in filter:
            answer += ch

    # 3) new_id에서 마침표(.)가 2번이상 연속된 부분을 하나의 마치표(.)로 치환합니다
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4) new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다
    answer = answer.strip('.')
    
    # 5) new_id가 빈 문자열이라면, new_id에 "a" 를 대입합니다
    if answer == '':
        answer = 'a'
       
    # 6) new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한
    # 나머지 문자들을 모두 제거합니다
    if len (answer) > 15:
        answer = answer[:15]
    
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 마지막 마침표(.)를  제거합니다
    answer = answer.rstrip('.')
    
    # 7) new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될때까지
    # 반복해서 끝에 붙입니다
    while len(answer) <= 2:
        answer += answer[-1]
        
    '''
        - 문자열 인덱싱 : 지정한 위치의 글자 하나를 가져오기
        - 문자열은 개별문자 하나하나가 한 줄로 나열되어 있는 형다
        - 파이썬 인덱싱은 음수를 지원 한다
        - 0이 항상 첫번째 글자(요소)를 거리키고, 음수인덱스는 마지막부터 찾는다
        - "Hello" 에서 0번째 글짜는 "H" 이고, -1번째 글자는 "O" 이다
        
        - 문자열 더하기 : 숫자는 더하면 덧샘 연산을 처리하고, 문자열은 더하면 이어붙이기 
        
        - 대입연산자 기준으로 항상 우변부터 먼저 처리한다
        - 복합대입연산자는 좌변과 우변에 동일한 변수가 있을 경우를 줄여서 쓰는 형태이다
        - answer += answer[-1]  =>  answer = answer + answer[-1]
    '''


    print('{:30s}'.format(answer), end= '\t')
    return answer

print("bat.y.abcdefghi" == solution("...!@Bat#*..Y.abcdefghijklm"))
print("z--" == solution("z-=.^."))
print("aaa" == solution("=.="))
print("123_.def" == solution("123_.def"))
print("abcdefghijklmn" == solution("abcdefghijklmn.p"))