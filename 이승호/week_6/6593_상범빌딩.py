from collections import deque

dx = [0,0,0,0,1,-1]
dy = [1,-1,0,0,0,0]
dz = [0,0,1,-1,0,0]


def is_valid(x,y,z):
    return 0 <= x < floor and 0 <= y < r and 0 <= z < c


while True:
    floor, r, c = map(int, input().split())
    if (floor, r, c) == (0, 0, 0):
        break
    arr = [[[0]*c for _ in range(r)] for _ in range(floor)]
    for k in range(floor):  # 벽이면 1, 그외에 0
        for i in range(r):
            tmp = list(input())
            for j in range(c):
                if tmp[j] == '#':
                    arr[k][i][j] = 1
                elif tmp[j] == 'S':  # 스타트 저장
                    start = (k,i,j)
                elif tmp[j] == 'E':  # 탈출구 저장
                    escaped = (k,i,j)
        input()
    visited = [[[0]*c for _ in range(r)] for _ in range(floor)]
    visited[start[0]][start[1]][start[2]] = 1
    stack = deque()
    stack.append(start)
    check = 0
    while stack:
        l = len(stack)
        for _ in range(l):
            x, y, z = stack.popleft()
            if (x,y,z) == escaped:
                check = 1
                break
            for d in range(6):
                nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]
                if is_valid(nx,ny,nz) and arr[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    stack.append((nx,ny,nz))
        if check:
            break
    if check:
        print(f'Escaped in {visited[escaped[0]][escaped[1]][escaped[2]]-1} minute(s).')
    else:
        print(f'Trapped!')



'''
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E


'''