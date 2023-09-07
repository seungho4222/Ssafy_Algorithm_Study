''' 벽에 둘러싸인 배열에서 로봇좌표 계산용 
-1 -1 -1 -1 -1 -1 -1
-1  4             -1  행번호 반대로!!
-1  3             -1
-1  2             -1
-1  1  2  3  4  5 -1
-1 -1 -1 -1 -1 -1 -1
'''
# 방향 숫자로 입력
news = {'E':1, 'W':2, 'S':3, 'N':4}
# 회전방향별 90도 회전후 방향
dir_L = {1:4, 4:2, 2:3, 3:1}
dir_R = {1:3, 3:2, 2:4, 4:1}

col, row = map(int, input().split())
N, M = map(int, input().split())  # N: 로봇 수, M: 명령 수
# 벽(-1)으로 둘러싸기
arr = [[-1] * (col + 2)]
for i in range(row):
    arr.append([-1] + [0]*col + [-1])
arr += [[-1] * (col + 2)]
# 방향 {동:1, 서:2, 남:3, 북:4}
robot = [[]]  # 로봇번호를 인덱스로 하는 좌표 저장
for i in range(N):
    c, r, d = input().split()  # 로봇 시작 위치 및 방향 입력
    c, r = int(c), int(r)
    arr[row+1-r][c] = [i+1, news[d]]  # 배열에 로봇번호, 방향 저장
    robot.append([row+1-r,c])
# print(arr)
# print(robot)
# 명령 저장 {L:왼쪽90도, R: 오른쪽90도, F:전진}
command = []
for i in range(M):
    num, com, repeat = input().split()
    command.append([int(num),com,int(repeat)])
# print(command)
# 명령 시작 {0: 'OK', 1: 'Robot X crashes into the wall', 2: 'Robot X crashes into robot Y'}
result = 0
for si in command:  # 시뮬레이션 시작
    x, y = robot[si[0]]
    for _ in range(si[2]):
        if si[1] == 'L':
            arr[x][y][1] = dir_L[arr[x][y][1]]
        elif si[1] == 'R':
            arr[x][y][1] = dir_R[arr[x][y][1]]
        elif si[1] == 'F':
            if arr[x][y][1] == 1:
                nx, ny = x + 0, y + 1
                if arr[nx][ny] == 0:
                    arr[x][y] = 0
                    arr[nx][ny] = [si[0], 1]
                    x, y = nx, ny
                    robot[si[0]] = [nx, ny]
                elif arr[nx][ny] == -1:
                    result = (1, si[0])
                    break
                else:
                    result = (2, si[0], arr[nx][ny][0])
                    break
            elif arr[x][y][1] == 2:
                nx, ny = x + 0, y - 1
                if arr[nx][ny] == 0:
                    arr[x][y] = 0
                    arr[nx][ny] = [si[0], 2]
                    x, y = nx, ny
                    robot[si[0]] = [nx, ny]
                elif arr[nx][ny] == -1:
                    result = (1, si[0])
                    break
                else:
                    result = (2, si[0], arr[nx][ny][0])
                    break
            elif arr[x][y][1] == 3:
                nx, ny = x + 1, y + 0
                if arr[nx][ny] == 0:
                    arr[x][y] = 0
                    arr[nx][ny] = [si[0], 3]
                    x, y = nx, ny
                    robot[si[0]] = [nx, ny]
                elif arr[nx][ny] == -1:
                    result = (1, si[0])
                    break
                else:
                    result = (2, si[0], arr[nx][ny][0])
                    break
            elif arr[x][y][1] == 4:
                nx, ny = x - 1, y + 0
                if arr[nx][ny] == 0:
                    arr[x][y] = 0
                    arr[nx][ny] = [si[0], 4]
                    x, y = nx, ny
                    robot[si[0]] = [nx, ny]
                elif arr[nx][ny] == -1:
                    result = (1, si[0])
                    break
                else:
                    result = (2, si[0], arr[nx][ny][0])
                    break
    if result:
        break
if result == 0:
    print("OK")
elif result[0] == 1:
    print(f'Robot {result[1]} crashes into the wall')
elif result[0] == 2:
    print(f'Robot {result[1]} crashes into robot {result[2]}')


'''
5 4
2 2
1 1 E
5 4 W
1 F 7
2 F 7

'''