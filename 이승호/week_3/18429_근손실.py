# 중량 500 기준, 하루에 k만큼 감소
# 각각의 중량 증가량을 가진 N개의 키트 -> N일동안 하루에 1개씩만 가능
# N일동안 중량 500이상 유지 목표

N, K = map(int, input().split())
# N개의 운동키트 중량 증가량
A = list(map(int, input().split()))
# 3대 500치는 사람
weight = 500

# 훈련 시작
def training(w, n, visited):
    ans = 0
    # 500 아래로 떨어지면 안됨
    if w < weight:
        return 0
    # N일동안 500이상 유지!
    if n == N:
        return 1
    # 탐색 시작
    for i in range(N):
        if i not in visited:
            new_visited = visited + [i]
            ans += training(w-K+A[i],n+1,new_visited)
    return ans


print(training(500,0,[]))