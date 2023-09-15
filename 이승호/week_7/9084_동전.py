def f():
    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] += dp[i - coin]
    return dp[M]


T = int(input())
for _ in range(T):
    N = int(input())  # 동전의 가지 수
    coins = list(map(int, input().split()))
    M = int(input())  # 동전으로 만들어야 할 값

    dp = [0] * (M+1)
    dp[0] = 1
    print(f())
