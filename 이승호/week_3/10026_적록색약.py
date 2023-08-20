# 총 구역 개수 / 적록색약 시각의 구역 개수
N = int(input())    # 구역 N * N
rgb = [list(input()) for _ in range(N)]     # 그림 색깔 배열 (R, G, B)

# 적록색약 아닌 경우
def RGB_no():
    matrix = [[0]*N for _ in range(N)]
    cnt = 0
    # 배열 순회
    for i in range(N):
        for j in range(N):
            # 방문한적 없으면
            if not matrix[i][j]:
                matrix[i][j] = 1
                stack = [(i, j)]
                # 주변 탐색
                while stack:
                    r, c = stack.pop(0)
                    for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                        nr, nc = r + dr, c + dc
                        # 같은 색 있으면 방문 체크하고 스택쌓기
                        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 0 and rgb[nr][nc] == rgb[r][c]:
                            matrix[nr][nc] = 1
                            stack += [(nr,nc)]
                # 탐색 끝나면 카운트 + 1
                cnt += 1
    return cnt

# 적록색약인 경우
def RGB():
    matrix = [[0]*N for _ in range(N)]
    cnt = 0
    # 배열 순회
    for i in range(N):
        for j in range(N):
            # 파란색인 경우
            if not matrix[i][j] and rgb[i][j] == 'B':
                matrix[i][j] = 1
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop(0)
                    for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                        nr, nc = r + dr, c + dc
                        # 파란색만 체크
                        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 0 and rgb[nr][nc] == rgb[r][c]:
                            matrix[nr][nc] = 1
                            stack += [(nr,nc)]
                cnt += 1
            # 적녹색인 경우
            elif not matrix[i][j] and rgb[i][j] in 'RG':
                matrix[i][j] = 1
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop(0)
                    for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                        nr, nc = r + dr, c + dc
                        # 적녹색만 체크
                        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 0 and rgb[nr][nc] in 'RG':
                            matrix[nr][nc] = 1
                            stack += [(nr,nc)]
                cnt += 1
    return cnt


print(RGB_no(), RGB())