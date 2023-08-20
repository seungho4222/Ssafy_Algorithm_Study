# 투에모스 문자열
def Thue_morse(k):
    # 0 과 1 출력하는 경우
    if k == 1:
        return 0
    if k == 2:
        return 1
    # 최대 2의 몇승에 인접한지 계산
    n = 0
    while k > 2**n:
        n += 1
    # 2의 n승만큼 규칙 반복
    # ex) 5, 6, 7, 8 => 1, 2, 3, 4
    if k // 2 == 2 ** (n-1):    # k//2가 2의n승과 동일값이면 따로 계산
        x = 2 ** (n-1)
    else:       # 2의 n승으로 나눈 나머지로 재귀
        x = k % (2 ** (n-1))

    # 재귀값의 반대값 출력
    if Thue_morse(x) == 0:
        return 1
    else:
        return 0


N = int(input())
print(Thue_morse(N))