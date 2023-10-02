t = input()  # 전체 문자열
p = input()  # 폭발 문자열

last = p[-1]  # 폭발 문자열 마지막 문자
m = len(p)  # 폭발 문자열 길이


def bomb():
    stack = []
    for char in t:  # 전체 문자열 확인
        stack.append(char)  # 스택 추가
        if char == last and ''.join(stack[-m:]) == p:  # 확인한 문자가 폭발 문자열 마지막 문자이고, 스택에 폭발 문자열이 있으면
            del stack[-m:]  # 폭발

    ans = ''.join(stack)  # 폭발 후 남은 문자열
    if ans == '':
        return 'FLURA'
    else:
        return ans


print(bomb())



''' 내 오답
t = list(input())  # 전체 문자열
p = input()  # 폭발 문자열

m = len(p)

skip_table = {}
for i in range(m - 1):
    skip_table[p[i]] = m - i - 1


def boyer_moore():
    global t
    n = len(t)
    i = m - 1
    j = m - 1
    while i < n:
        if t[i] == p[j]:
            if j == 0:
                del t[i:i+m]
                n = len(t)
                if i < m - 1:
                    i = m - 1
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            skip_val = skip_table.get(t[i], m)
            i += skip_val
            j = m - 1


boyer_moore()

if len(t) == 0: 
    print('FRULA')
else:
    print(''.join(t))
'''