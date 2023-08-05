# 소수 체크
def prime_check(x):
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 중간값 기준 소수 계산(골드바흐 파티션이 아닐경우 줄이고 늘려가면서)
    down, up = n//2, n//2
    # 골드바흐 파티션 계산
    while True:
        # 중간갑 기준 내려가면서 소수 찾기
        for d in range(down,0,-1):
            if prime_check(d): break
        # 중간값 기준 올라가면서 소수 찾기
        for u in range(up,n):
            if prime_check(u): break
        # 파티션 확인
        if d + u == n: print(d, u); break
        # 파티션 아닐경우 값 변경해서 반복
        down -= 1
        up += 1