from heapq import heappush, heappop

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

D = [1e9] * (V+1)

def dijkstra(s):
    pq = []
    heappush(pq, (0, s))
    D[s] = 0
    while pq:
        w, v = heappop(pq)
        if D[v] < w:
            continue
        for u, uw in graph[v]:
            cost = w + uw
            if D[u] > cost:
                D[u] = cost
                heappush(pq, (cost, u))
    return D

result = dijkstra(start)
for i in range(1, V+1):
    if result[i] == 1e9:
        print('INF')
    else:
        print(result[i])