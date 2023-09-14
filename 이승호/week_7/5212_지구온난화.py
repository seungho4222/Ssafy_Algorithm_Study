from collections import deque

# 1. 지도 주변 바다로 둘러싸기
row, col = map(int, input().split())  # 지도 크기
arr = [['.' for _ in range(col+2)]]
for k in range(row):  # 땅: 'X', 바다: '.'
    arr.append(['.'] + list(input()) + ['.'])
arr.append(['.']*(col+2))

# 2. 3면 이상이 바다인 땅의 좌표 구하기
tmp = deque()  # 잠기는 땅 좌표 저장소
for r in range(row+2):  # 바다로 둘러쌓았기 때문에 행,열 +2
    for c in range(col+2):
        if arr[r][c] == 'X':  # 땅 주변만 잠기는지 확인
            check = 0
            for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:  # 델타 탐색
                nr, nc = r + dr, c + dc
                if 0 <= nr < row+2 and 0 <= nc < col+2 and arr[nr][nc] == '.':
                    check += 1  # 주변이 바다면 체크
            if check >= 3:  # 3면 이상 바다면 해당 땅 좌표 저장
                tmp.append([r,c])

# 3. 50년 후 잠기는 땅 바다로 변경
for r, c in tmp:
    arr[r][c] = '.'

# 4. 배열의 상하좌우에 바다가 일직선으로 있으면 출력 X
rectangle = [0, row+2, 0, col+2]  # [위, 아래, 왼쪽, 오른쪽] -> 해당 좌표부터는 땅이 있다

for i in range(row+2):  # 위쪽 행부터
    see = 0
    for j in range(col+2):
        if arr[i][j] == 'X':
            see = 1
            break
    if see:
        rectangle[0] = i
        break

for i in range(row+1,-1,-1):  # 아래쪽 행부터
    see = 0
    for j in range(col+2):
        if arr[i][j] == 'X':
            see = 1
            break
    if see:
        rectangle[1] = i
        break

for j in range(col+2):  # 왼쪽 열부터
    see = 0
    for i in range(row+2):
        if arr[i][j] == 'X':
            see = 1
            break
    if see:
        rectangle[2] = j
        break

for j in range(col+1,-1,-1):  # 오른쪽 열부터
    see = 0
    for i in range(row+2):
        if arr[i][j] == 'X':
            see = 1
            break
    if see:
        rectangle[3] = j
        break

# print(arr)
# print(rectangle)

# 5. 모든 섬을 포함하는 가장 작은 직사각형 출력
for r in range(rectangle[0], rectangle[1]+1):
    for c in range(rectangle[2],rectangle[3]+1):
        print(arr[r][c], end='')
    print()
    