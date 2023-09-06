def lcm(x, y):
    def gcd(x,y):
        while y:
            x, y = y, x % y
        return x 
    return x * y // gcd(x,y)


T = int(input())
for tc in range(1, T+1):
    M, N, x, y = map(int, input().split())  # (M, N)은 마지막해, (x, y)는 찾아야 하는 해
    a, b = 1, 1  # 첫번째 해 표현
    cnt = 1  # 첫번째 해
    check = False  # 체크 기본값
    if (x, y) == (1, 1):  # 찾는 값이 첫번째 해이면 출력
        print(1)
    else:  # 아니면 계산
        while a != M or b != N:
            if (a == M and b > N) or (a > M and b == N):
                break
            a += 1  # M 이하면 1증가, 초과하면 1변경
            if a > M: a = 1
            b += 1  # N 이하면 1증가, 초과하면 1변경
            if b > N: b = 1
            cnt += 1  # 햇수 카운트
            if (a, b) == (x, y):  # 해를 찾았다면 체크 트루 변경 후 종료
                check = True
                break
        if check:  # 해를 찾았는지 여부
            print(cnt)
        else:
            print(-1)