N, M = map(int, input().split())
nums = [num for num in range(1, N+1)]
selected = [0] * N

def perm(i):
    # 종료조건
    if i == M:
        for k in selected:
            if not k:
                print()
                return
            else:
                print(k, end=' ')
        print()
        return
    # 순열 고르기
    for j in range(N):
        if selected[i-1] > nums[j]:
            continue
        selected[i] = nums[j]
        perm(i+1)
        selected[i] = 0

perm(0)