N, M = map(int, input().split())  # N: 입국심사대 수, M: 몇명
arr = [int(input()) for _ in range(N)]  # 각 심사시간

l, r = min(arr), max(arr) * M
ans = r  # 총 심시시간 최대값 시작

while l <= r:  # 이분탐색
    total = 0  # 심사 가능 인원
    mid = (l + r) // 2  # 총 심사 시간

    for i in range(N):
        total += mid // arr[i]  # 각 심사대에서 mid 시간 동안 수속 가능한 인원 수 체크

    if total >= M:  # M 명 이상 수속가능하면 출력값 비교 갱신
        r = mid -1  # 적은 시간으로 가능한지 탐색
        ans = min(mid, ans)

    else:  # 수속 불가 -> 심사시간 더 필요
        l = mid + 1

print(ans)