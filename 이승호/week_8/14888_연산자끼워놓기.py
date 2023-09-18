N = int(input())  # 수의 개수
nums = list(map(int, input().split()))  # 숫자
operator = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈
op = []
d = {0:'+', 1:'-', 2:'*', 3:'/'}
for i in range(4):
    for _ in range(operator[i]):
        op.append(d[i])

used = [0] * (N-1)
max_v = -1e10
min_v = 1e10

def calc(idx, total):
    global max_v, min_v
    if idx == N-1:
        max_v = max(max_v, total)
        min_v = min(min_v, total)
        return
    check = []
    for i in range(N-1):
        if used[i] == 0 and op[i] not in check:
            used[i] = 1
            check.append(op[i])
            calc(idx+1, oper(total, op[i], nums[idx+1]))
            used[i] = 0


def oper(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num1 < 0:
            return -((-num1) // num2)
        else:
            return num1 // num2

calc(0,nums[0])
print(max_v)
print(min_v)