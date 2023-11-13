N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def subset(idx, list):
    if idx == M:
        print(*list)
        return
    
    for i in range(N):
        subset(idx + 1, list + [nums[i]])


subset(0, [])
