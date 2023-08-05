def solution(s):
    answer = True
    check = []
    for i in s:
        if check == []:
            if i == '(':
                check += [i]
            elif  i == ')':
                answer = False
                return answer
        elif check:
            if i == '(':
                check += [i]
            elif i == ')':
                check.pop()
    if check != []:
        answer = False
    return answer

print(solution('(hello)'))