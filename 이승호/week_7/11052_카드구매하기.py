N = int(input())  # 구매하려는 카드 수
p = [0] + list(map(int, input().split()))  # 카드 가격

memo = [0] * (N+1)  # 메모이제이션

for i in range(1, N+1):  # 카드개수별 (1 ~ N) 최대값 메모
    for j in range(1, i+1):  # i를 만들 수 있는 메모값 조합 반복
        memo[i] = max(memo[i], p[j] + memo[i-j])  # 최대값 저장

print(memo[N])