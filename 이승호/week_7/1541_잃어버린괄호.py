formula = input()  # 계산식

del_minus = formula.split('-')  # - 로 스플릿 => 숫자 및 덧셈 계산식으로 구분
                                # 55-50+40 => 55, 50+40
ans = []  # - 로 구분한 덧셈식들을 계산한 숫자 저장
for f_plus in del_minus:  # 덧셈식 반복
    tmp = 0
    del_flus = f_plus.split('+')  # + 로 스플릿
    for num in del_flus:  # 연산자로 스플릿을 두번 했으니 남은 건 숫자뿐 !!
        tmp += int(num)  # + 스플릿한 계산식은 모두 더해주고
    ans.append(tmp)  # 덧셈식 결과값 저장
    
result = ans[0]  # 덧셈식 결과값의 첫번째 수에서 나머지 수를 전부 빼주면 최소값 !!
if len(ans) >= 2:  # 두번째부터 빼주기
    for k in range(1, len(ans)):
        result -= ans[k]

print(result)
