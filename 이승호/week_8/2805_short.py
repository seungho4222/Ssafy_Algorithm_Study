N, M = map(int, input().split())
tree = sorted(list(map(int, input().split())), reverse=True) + [0]  # 내림차순 정렬

cnt = 1  # 자르려는 기준 높이의 나무 인덱스번호
ans = 0  # 자르려는 나무 길이
while cnt < N + 1 and ans < M:  # 자르려는 나무가 가져갈 나무길이보다 작으면 다음 높이의 나무까지 확인
    ans += cnt * (tree[cnt-1] - tree[cnt])
    cnt += 1

k = abs(M - ans) // (cnt-1)
print(tree[cnt-1] + k)
