N = int(input())
dp = [0] * (N+1)
for i in range(1, N+1):
    if i == 1:
        dp[1] = 'SK'
    elif i == 2:
        dp[2] = 'CY'
    elif i == 3:
        dp[3] = 'SK'
    elif i == 4:
        dp[4] = 'SK'
    elif i == 5:
        dp[5] = 'SK'
    elif i == 6:
        dp[6] = 'SK'
    elif i == 7:
        dp[7] = 'CY'
    elif i == 8:
        dp[8] = 'SK'

if N > 8:
    for i in range(9, N+1):
        if (dp[i-2] == 'SK' and dp[i-4] =='SK' and dp[i-5] == 'SK') or (dp[i-4] == 'SK' and dp[i-6] == 'SK' and dp[i-7] == 'SK') or (dp[i-5] == 'SK' and dp[i-7] == 'SK' and dp[i-8] =='SK'):
            dp[i] = 'SK'
        else:
            dp[i] = 'CY'
print(dp[N])

# 1        3        4
# 2 4 5   4 6 7    5 7 8

# 1 SK
# 2 CY
# 3 SK
# 4 SK

# 5 SK
# 6 SK
# 7 CY
# 8 SK
# 9 CY
# 10 SK
# 11 SK