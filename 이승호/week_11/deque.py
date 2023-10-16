from collections import deque

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

W, H = map(int, input().split())  # W: 열, H: 행
laser = []  # 2개의 C 좌표
arr = [[0] * W for _ in range(H)]

for r in range(H):
    row = list(input())
    for c in range(W):
        if row[c] == '*':  # 벽이면 1로 변경
            arr[r][c] = 1
        elif row[c] == 'C':
            laser.append([r,c])

adjl = [[[] for _ in range(W)] for _ in range(H)]
D = [[10000] * W for _ in range(H)]

for r in range(H):
    for c in range(W):
        if arr[r][c] == 0:  # 벽만 아니면
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == 0:
                    adjl[r][c].append([d, nr, nc])  # 연결 방향 및 좌표 저장


def dijkstra(sr, sc):
    q = deque()
    q.append([-1, sr, sc, -1])
    D[sr][sc] = 0

    while q:
        w, vr, vc, d_memo = q.popleft()
        if D[vr][vc] < w:
            continue
        for d, ur, uc in adjl[vr][vc]:
            cost = w
            if d_memo != d:  # 방향 꺾였다
                cost += 1  # 거울 설치
            if cost <= D[ur][uc]:
                D[ur][uc] = cost
                q.append([cost, ur, uc, d])


dijkstra(laser[0][0], laser[0][1])

print(D[laser[1][0]][laser[1][1]])
