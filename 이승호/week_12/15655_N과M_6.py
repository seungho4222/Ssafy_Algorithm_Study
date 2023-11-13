N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def subset(idx, list):
    if len(list) == M:
        print(*list)
        return
    
    for i in range(idx, N):
        subset(i + 1, list + [nums[i]])


subset(0, [])
