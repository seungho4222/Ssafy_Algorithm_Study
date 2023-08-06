def solution(s):
    # 기본 True로 설정
    answer = True
    # 괄호 확인 장소
    check = []
    for i in s:
        # 체크 비어있을 경우
        if check == []:
            if i == '(':
                check += [i]
            # 괄호 짝이 안맞기 때문에 False 리턴
            elif  i == ')':
                answer = False
                return answer
        # 체크에 원소 있을 경우
        elif check:
            if i == '(':
                check += [i]
            # 체크에는 '('만 있기 때문에 괄호 짝 맞음 => 마지막원소 제거
            elif i == ')':
                check.pop()
    # 마지막 글자가 '('로 들어올 경우 방지
    if check != []:
        answer = False
    return answer

print(solution('(hello)'))