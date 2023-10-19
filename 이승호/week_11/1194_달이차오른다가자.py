from collections import deque

alp = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f'}
alp_idx = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
x_alp = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F'}

dr = [-1,1,0,0]
dc = [0,0,-1,1]

N, M = map(int, input().split())
maze = []
goal = deque()
visited = [[[True for _ in range(6)]] * M for _ in range(N)]
onemore = [[0] * M for _ in range(N)]

for r in range(N):
    col = input()
    maze.append(col)
    for c in range(M):
        if col[c] == '0':
            sr, sc = r, c  # 시작 위치
        elif col[c] == '1':
            goal.append((r, c, 0, deque()))  # 목표 위치, 이동거리


def check(cr, cc):
    for kk in range(6):
        if visited[cr][cc][kk] == False:
            return False
    return True



def move():
    while goal:
        r, c, w, lst = goal.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:

                value = maze[nr][nc]
                if value =='#':
                    continue
                elif value in ['A', 'B', 'C', 'D', 'E', 'F'] and value not in lst and alp[value] not in lst:
                    lst.append(value)
                    goal.append((nr, nc, w + 1, lst))
                    visited[nr][nc][alp_idx[value]] = False
                    lst.pop()
                elif value in ['a', 'b', 'c', 'd', 'e', 'f'] and value not in lst:
                    if x_alp[value] in lst:
                        visited[nr][nc][alp_idx[x_alp[value]]] = True
                    lst.append(value)
                    goal.append((nr, nc, w + 1, lst))
                    lst.pop()
                if value == '0':
                    if ('A' in lst and alp['A'] not in lst) or ('B' in lst and alp['B'] not in lst) or ('C' in lst and alp['C'] not in lst) or ('D' in lst and alp['D'] not in lst) or ('E' in lst and alp['E'] not in lst) or ('F' in lst and alp['F'] not in lst):
                        goal.append((nr, nc, w + 1, lst))
                        continue 
                    return w + 1
                goal.append((nr, nc, w + 1, lst))
    return -1

print(move())