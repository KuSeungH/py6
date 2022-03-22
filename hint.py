# hint.py
# 원하는 문자만 남기고 나머지 모두 제거하기

test = 'abcde12'              # 원하는 문자
nwe_id = "1a2b3c4d5e6f"     # 입력받는 문자
answer = ''                 # 원하는 문자만 걸러내서 만든 결과

for ch in nwe_id:   # nwe_id의 각 글자가
    if ch in test:  # test에 포함되어 있다면 
        answer += ch    # answer 에 더하기
                    # test에 포함하지 않는 글자는 제외된다
print(nwe_id)
print(answer)