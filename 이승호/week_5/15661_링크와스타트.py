N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = 1e9
for i in range(1, 1<<(N-1)):
    start = []
    link = []
    for j in range(N):
        if i & (1<<j): start.append(j)
        else: link.append(j)
    if len(start) > 1 and len(link) > 1:
        start_stat = 0
        for i in start:
            for j in start:
                if i != j: start_stat += arr[i][j]
        link_stat = 0
        for i in link:
            for j in link:
                if i != j: link_stat += arr[i][j]
        min_v = min(min_v, abs(start_stat - link_stat))
print(min_v)