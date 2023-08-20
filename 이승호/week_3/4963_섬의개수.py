while True:
    # w: 지도의 너비, h: 높이
    w, h = map(int, input().split())
    # 케이스 종료 조건
    if w == 0 and h == 0:
        break
    # 지도 배열
    arr = [list(map(int, input().split())) for _ in range(h)]
    # 섬의 개수
    cnt = 0
    # 탐색
    for r in range(h):
        for c in range(w):
            # 땅이면 주변 탐색 시작
            if arr[r][c] == 1:
                stack = []
                # 주변 땅 없을때까지
                while True:
                    # 방문한 땅 0 체크
                    arr[r][c] = 0
                    # 8방향 탐색
                    for dr, dc in [[-1,0],[1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,-1],[-1,1]]:
                        nr, nc = r + dr, c + dc
                        # 범위 내 델타값이 땅이면 기준 좌표 스택 쌓고 델타값을 기준 좌표로 변경
                        if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1:
                            stack += [(r, c)]
                            r, c = nr, nc
                            break
                    # 델타탐색 실패한 경우 스택 꺼내서 탐색
                    else:
                        if stack:
                            r, c = stack.pop()
                        # 스택 비었으면 탐색 종료
                        else: break
                # 더 이상 땅 없으면 탐색한 섬 카운트 + 1
                cnt += 1
    print(cnt)