N, M = map(int, input().split())
tree = sorted(list(map(int, input().split())), reverse=True)  # 내림차순 정렬

cnt = 0  # 자르려는 기준 높이의 나무 인덱스번호
ans = 0  # 자르려는 나무 길이
while cnt < N-1 and ans < M:  # 자르려는 나무가 가져갈 나무길이보다 작으면 다음 높이의 나무까지 확인
    cnt += 1
    ans += cnt * (tree[cnt-1] - tree[cnt])

if ans > M:  # 높이 위로 조절
    k = (ans-M) // cnt
    print(tree[cnt] + k)

else:  # 가장 낮은 나무까지 자르는 경우는 높이 아래로 조절
    k = (M-ans) // (cnt + 1)  # 몫
    r = (M-ans) % (cnt + 1)  # 나머지
    if r:
        print(tree[cnt] - k - 1)
    else:
        print(tree[cnt] - k)

        

'''
4 17
1 3 3 10

'''