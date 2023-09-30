from heapq import heappush, heappop


def dijkstra(s):
    D = [1e9] * (N+1)
    pq = []
    heappush(pq, [0,s])
    D[s] = 0

    while pq:
        w, v = heappop(pq)
        if D[v] < w:
            continue
        for u, uw in graph[v]:
            cost = w + uw
            if D[u] > cost:
                D[u] = cost
                heappush(pq, [cost, u])
    result.append(D)


N, M, X = map(int, input().split())  # N: 사람 번호, M: 간선 수, X: 목표 집
graph = [[] for _ in range(N+1)]
for _ in range(M):
    f, t, w = map(int, input().split())  # from, to, weight
    graph[f].append([t, w])

result = [[0] * (N+1)]

for i in range(1, N+1):
    dijkstra(i)

max_v = 0  # 왕복 가중치가 가장 큰 값 출력
for r in range(1, N+1):
    cost = result[r][X] + result[X][r]
    if cost < 1e9:
        max_v = max(max_v, cost)

print(max_v)