N, M = map(int, input().split())
nums = [num for num in range(1, N+1)]


def subset(idx, list, visited):
    if idx == M:
        print(*list)
        return
    
    for i in nums:
        if i not in visited:
            subset(idx + 1, list + [i], visited + [i])


subset(0, [], [])
