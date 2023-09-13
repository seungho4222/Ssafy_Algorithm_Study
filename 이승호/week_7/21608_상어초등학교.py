satisfation = {0:0, 1:1, 2:10, 3:100, 4:1000}  # 만족도 점수표
d = [[0,1],[1,0],[0,-1],[-1,0]]  # 델타 탐색

def my_seat(iwant):
    check = 0  # 어떤자리 앉아야할지 비교할 값 초기화
    tmp = [20,20]  # 앉을 자리 좌표 초기화
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:  # 빈 자리만 탐색
                vs_check = 0  # 해당 자리 주변 점수 체크
                r, c = i, j
                for dr, dc in d:  # 델타
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if arr[nr][nc] == 0:
                            vs_check += 1  # 주변 빈칸이면 + 1
                        elif arr[nr][nc] in iwant:
                            vs_check += 5  # 주변 좋아하는 학생이면 + 5
                if check < vs_check:  # 주변에 좋아하는 학생 및 빈칸이 더 많으면 값 변경
                    check = vs_check
                    tmp = [i, j]
                elif check == vs_check:  # 해당 칸이 여러개라면
                    if tmp[0] > i:  # 행번호 우선
                        tmp = [i, j]
                    elif tmp[0] == i and tmp[1] > j:  # 열번호 우선
                        tmp = [i, j]
    return tmp


N = int(input())
arr = [[0]*N for _ in range(N)]  # 교실크기 N x N
table = [0] * (N**2 + 1)  # 좋아하는 학생 조사 결과 (인덱스: 학생번호)

for _ in range(N**2):  # 학생 수 N**2
    s, *want = map(int, input().split())  # 학생번호, 좋아하는 학생 4명 리스트
    table[s] = want  # 좋아하는 학생 저장
    x, y = my_seat(want)  # 학생이 앉을 자리 좌표 구하기
    arr[x][y] = s  # 해당 좌표에 학생번호 입력

result = 0  # 만족도 총합
for r in range(N):
    for c in range(N):
        cnt = 0  # 주변에 좋아하는 학생 몇명인지?
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                # 델타 번호가 기준번호의 좋아하는 학생번호이면 카운트
                if arr[nr][nc] in table[arr[r][c]]:
                    cnt += 1
        result += satisfation[cnt]  # 만족도 점수표 계산

print(result)
