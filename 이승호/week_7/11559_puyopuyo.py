from collections import deque

arr = [list(input()) for _ in range(12)]  # 6개 문자열 * 12줄

d = [[0,1],[1,0],[0,-1],[-1,0]]  # 4방향 델타

def puyo():  # 뿌요뿌요 연결 체크
    check = 0
    for i in range(11,-1,-1):
        for j in range(6):
            if arr[i][j] != '.':  # 빈공간이 아니면
                q = deque()  # 너비우선 탐색용
                save = deque()  # 탐색종료 후 값 변경용
                q.append([i, j])
                save.append([i, j])
                cnt = 1  # 뿌요 연결 개수
                while q:
                    r, c = q.popleft()
                    for dr, dc in d:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < 12 and 0 <= nc < 6 and arr[r][c] == arr[nr][nc] and [nr,nc] not in save:
                            q.append([nr,nc])  # 탐색 계속 진행
                            save.append([nr,nc])  # 탐색 성공한 좌표는 따로 저장
                            cnt += 1
                if cnt >= 4:  # 뿌요 4개 이상 연결됐다 !!
                    check = 1  # 연결 성공 체크
                    for r, c in save:  # 뿌요는 빈공간으로 변경
                        arr[r][c] = '.'
    return check

def sink():  # 뿌요 성공했으니 모든 뿌요 아래로 내리기
    for j in range(6):
        for i in range(10,-1,-1):
            if arr[i][j] != '.':
                for n in range(11,i,-1):
                    if arr[n][j] == '.':
                        arr[i][j],arr[n][j] = arr[n][j],arr[i][j]

result = 0  # 총 연쇄 카운트
while True:
    if puyo():  # 뿌요 성공했으면
        sink()  # 뿌요 떨어진다
        result += 1  # 연쇄 카운트 + 1
    else:
        break

print(result)
