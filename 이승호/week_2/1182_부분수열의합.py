N, S = map(int, input().split())
seq = list(map(int, input().split()))

ans = 0
for i in range(1<<N):
    temp = []
    for j in range(N):
        if i & (1<<j):
            temp += [seq[j]]
    if temp and sum(temp) == S:
        ans += 1

print(ans)


'''
5 0
-7 -3 -2 5 8

'''