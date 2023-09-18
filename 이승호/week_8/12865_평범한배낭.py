# 동적계획법 적용 - 상향식 최적해 알고리즘
def product():
    # 행: 물건 개수
    for i in range(1, N+1):
        # 열: 무게
        for j in range(1, K+1):
            # 무게가 i번째 크기보다 작을 경우 i번째 포함 불가 => i번째를 뺀(i-1) 최대가치
            if size[i] > j:
                dp[i][j] = dp[i-1][j]
            # i번째 크기를 포함할 수 있는 경우 => 포함하는 경우와 포함하지 않는 경우의 최대값 저장
            else:
                dp[i][j] = max(dp[i-1][j - size[i]] + price[i], dp[i-1][j])
    # 물건 N개 중 무게가 K일때 최대값 출력
    return dp[N][K]


# N: 물건 개수, K: 최대 무게
N, K = map(int, input().split())
# 물건별 무게 및 가치(1 ~ N번)
size = [0] * (N+1)
price = [0] * (N+1)
for i in range(N):
    s, p = map(int, input().split())
    size[i+1] = s
    price[i+1] = p
# 최적해 배열
dp = [[0]*(K+1) for _ in range(N+1)]

print(product())