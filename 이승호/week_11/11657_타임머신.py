N, M = map(int, input().split())  # N: 도시 수, M: 버스 수
adjl = []
dist = [1e9] * (N+1)
dist[1] = 0
for _ in range(M):
    s, e, w = map(int, input().split())  # 시작도시, 도착도시, 가중치
    adjl.append((s, e, w))

check = False  # 무한반복 ??
for i in range(N):  # 처음 거리를 무한대로 설정 => N-1만큼 반복해야 모든 루트 확인 가능능
    for start, end, wt in adjl:
        if dist[start] != 1e9:
            distance = dist[start] + wt  # 1번에서의 거리
            if distance < dist[end]:  # 더 작은 경로다 !
                if i == N-1:  # 계속 작아진다 => 무한반복
                    check = True
                    break
                dist[end] = distance  # 경로 변경경

if check:
    print(-1)
else:
    for x in dist[2:]:
        if x == 1e9:
            print(-1)
        else:
            print(x)





# N, M = map(int, input().split())  # N: 도시 수, M: 버스 수
# adjl = {}

# for i in range(M):
#     adjl[i] = {}

# for _ in range(M):
#     s, e, wt = map(int, input().split())
#     adjl[s][e] = w


# def bellman(graph, start):
#     dist, pre = dict(), dict()
#     for node in graph:
#         dist[node] = float('inf')
#         pre[node] = None
#     dist[start] = 0

#     for i in range(N-1):
#         for node in graph:
#             for next in graph[node]:
#                 if dist[next] > dist[node] + graph[node][next]:
#                     dist[next] = dist[node] + graph[node][next]
#                     pre[next] = node
    
#     for node in graph:
#         if next in graph[node]:
#             if dist[next] > dist[node] + graph[node][next]:
#                 return -1
#     return dist