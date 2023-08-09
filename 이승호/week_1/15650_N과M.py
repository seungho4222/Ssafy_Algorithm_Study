N, M = map(int, input().split())
# 1~N까지의 배열 생성
nums = [num for num in range(1, N+1)]
# 배열 길이
n = 0
for _ in nums:
    n += 1
# 길이가 M인 수열 저장
seq = []
# 길이가 M인 수열 출력
for i in range(1<<N):
    subset = []
    cnt = 0
    for j in range(n):
        if i & (1<<j):
            subset += [nums[j]]
            cnt += 1
    if cnt == M:
        seq += [subset]

# 오름차순 정렬
# seq.sort()
# for i in seq:
#     print(*i)

# 버블 정렬
for k in range(len(seq)-1, 0, -1):
    for i in range(k):
        j = 0
        if seq[i][j] > seq[i+1][j]:
            seq[i], seq[i+1] = seq[i+1], seq[i]
            continue
        while seq[i][j] == seq[i+1][j]:
            j += 1
            if seq[i][j] > seq[i+1][j]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
for i in seq:
    print(*i)