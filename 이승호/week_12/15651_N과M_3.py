N, M = map(int, input().split())
nums = [num for num in range(1, N+1)]


def subset(idx, list):
    if idx == M:
        print(*list)
        return
    
    for i in nums:
        subset(idx + 1, list + [i])


subset(0, [])