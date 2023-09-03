N, M = map(int, input().split())  # N: 건물의 개수, M: 도로의 개수
road = [[] for _ in range(N+1)]  # 도로 인접리스트
for i in range(M):
    s, e = map(int, input().split())
    road[s].append(e)
    road[e].append(s)
bfs = [[N] * (N+1) for _ in range(N+1)]  # 각 도로를 기준점으로 하는 거리 입력
for i in range(1, N+1):
    visited = [0] * (N+1)  # 방문 기록
    visited[i] = 1
    bfs[i][i] = 0  # 기준점에 0 입력
    stack = [i]  # bfs 돌며 거리 입력
    while stack:
        k = stack.pop(0)
        for j in road[k]:
            if visited[j] == 0:
                visited[j] = 1  # 방문 체크하며
                bfs[i][j] = bfs[i][k] + 1  # 스택값에 연결돤 도로는 거리 + 1 입력
                stack.append(j)
result = [N*2] * N  # 거리 비교 값 (일단, 최대값 입력)
ans = []  # 출력값
for i in range(1, N):
    for j in range(i+1, N+1):  # i, j 는 치킨집 2개 건물 번호
        tmp = [0] * N
        for k in range(N):  # 치킨집 건물 수 만큼 반복
            tmp[k] = min(bfs[i][k+1]*2, bfs[j][k+1]*2)  # 치킨집 2개에서 각 건물별 왕복거리 최소값 갱신
        if sum(result) > sum(tmp):  # 왕복거리의 합이 적은 경우만 갱신(같은 경우 i, j가 1부터 시작했으므로 작은값 입력됨)
            result = tmp  # 거리 비교 값 갱신
            ans = [i, j, sum(tmp)]  # 출력값인(건물번호 i, j, 왕복거리값)
print(*ans)
