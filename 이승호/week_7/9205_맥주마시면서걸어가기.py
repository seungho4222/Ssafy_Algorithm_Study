from collections import deque


def dist(dx,dy,ax,ay):  # 맥주 20병으로 갈 수 있는지 확인
    return (abs(dx-ax) + abs(dy-ay)) <= 1000


T = int(input())
for tc in range(T):
    n = int(input())  # 편의점 수
    hx, hy = map(int, input().split())  # 집 좌표
    cs = deque()  # 편의점 좌표
    for _ in range(n):
        x, y = map(int, input().split())
        cs.append([x,y])
    fx, fy = map(int, input().split())  # 페스티벌 좌표

    beer = 20  # 1병당 50m까지 -> 1000m 걸어도 편의점 없으면 sad

    dq = deque()  # bfs 탐색
    dq.append([hx,hy])

    check = False  # 페스티벌 갈 수 있을까 ??

    while dq:
        tmp = deque()  # deque은 반복문에서 변경 못하므로 새 리스트에 저장해야 됨
        dx, dy = dq.popleft()  # bfs 탐색
        if dist(dx,dy,fx,fy):
            check = True  # 갈 수 있다 !!
            break
        for cx, cy in cs:
            if dist(dx,dy,cx,cy):
                dq.append([cx,cy])  # 편의점에 갈 수 있으면 덱에 저장
            else:
                tmp.append([cx,cy])  # 못가면 다음 탐색 대상
        cs = tmp  # 탐색할 편의점 변경

    if check:
        print('happy')
    else:
        print('sad')


'''
3
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
2
0 0
1000 5
2000 10
3000 15

'''