from collections import deque

row, col = map(int, input().split())  # 지도 크기
arr = [['.' for _ in range(col+2)]]  # 지도 바다로 둘러싸기
for k in range(row):
    arr.append(['.'] + list(input()) + ['.'])
arr.append(['.']*(col+2))
# print(arr)

tmp = deque()  # 잠기는 땅 좌표 저장

for i in range(row+2):
    for j in range(col+2):
        if arr[i][j] == 'X':
            r, c = i, j
            check = 0
            for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row+2 and 0 <= nc < col+2 and arr[nr][nc] == '.':
                    check += 1
            if check >= 3:
                tmp.append([i,j])

for i, j in tmp:  # 3면이상 바다인 육지 좌표 -> 바다로 변경
    arr[i][j] = '.'
# print(tmp)

# 위, 아래, 왼쪽, 오른쪽 기준 -> 해당 좌표부터는 땅이 있다
rectangle = [0,row+2,0,col+2]

for i in range(row+2):
    see = 0
    for j in range(col+2):
        if arr[i][j] == 'X':
            see = 1
            break
    if see:
        rectangle[0] = i
        break

for i in range(row+1,-1,-1):
    see = 0
    for j in range(col+2):
        if arr[i][j] == 'X':
            see = 1
            break
    if see:
        rectangle[1] = i
        break

for j in range(col+2):
    see = 0
    for i in range(row+2):
        if arr[i][j] == 'X':
            see = 1
            break
    if see:
        rectangle[2] = j
        break

for j in range(col+1,-1,-1):
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

for r in range(rectangle[0], rectangle[1]+1):
    for c in range(rectangle[2],rectangle[3]+1):
        print(arr[r][c], end='')
    print()