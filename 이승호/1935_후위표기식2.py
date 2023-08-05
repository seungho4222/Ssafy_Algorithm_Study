N = int(input())
postfix = input()
nums = [int(input()) for _ in range(N)]
# 알파벳 저장
search = []
# 포스트픽스 해당 숫자 저장
temp = []
# 알파벳 달라지면 다음 넘버 할당하기 위한 카운트
cnt = 0
for i in postfix:
    # 알파벳이고 처음 나온거면 서치 저장하고 해당 숫자 템프에 저장
    if i.isalpha() and i not in search:
        search += [i]
        temp += [nums[cnt]]
        cnt += 1
    # 알파벳인데 이전과 동일한 알파벳이면 해당 알파벳 숫자 템프에 저장
    elif i.isalpha() and i in search:
        temp += [nums[search.index(i)]]
    # 템프 뒷순서 숫자 2개 계산 후 삽입
    elif i == '+':
        temp += [temp.pop(-2) + temp.pop(-1)]
    elif i == '-':
        temp += [temp.pop(-2) - temp.pop(-1)]
    elif i == '*':
        temp += [temp.pop(-2) * temp.pop(-1)]
    elif i == '/':
        temp += [temp.pop(-2) / temp.pop(-1)]

print(f'{temp[0]:.2f}')
