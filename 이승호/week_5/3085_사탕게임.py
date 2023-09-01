from collections import deque
def c_check(c):  # 동일 행에서 교환한 두 사탕의 열 체크
    global max_v
    v = 1
    for i in range(N-1):
        if board[i][c] == board[i+1][c]:
            v += 1
            max_v = max(max_v, v)
        else: v = 1
    v = 1
    for i in range(N-1):
        if board[i][c+1] == board[i+1][c+1]:
            v += 1
            max_v = max(max_v, v)
        else: v = 1


def r_check(r):  # 동일 열에서 교환한 두 사탕의 행 체크
    global max_v
    v = 1
    for j in range(N-1):
        if board[r][j] == board[r][j+1]:
            v += 1
            max_v = max(max_v, v)
        else: v = 1
    v = 1
    for j in range(N-1):
        if board[r][j] == board[r][j+1]:
            v += 1
            max_v = max(max_v, v)
        else: v = 1


N = int(input())  # 보드 크기
board = [list(input()) for _ in range(N)]  # 사탕 배열
max_v = 0
tmp = []
for i in range(N): # 동일 행에서 교환
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            for k in zip(board):
                if list(k) not in tmp: tmp.extend(list(k))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
for j in range(N):  # 동일 열에서 교환
    for i in range(N-1):
        if board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            for k in board:
                if k not in tmp:
                    print(k)
                    tmp.append(k)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(tmp)

