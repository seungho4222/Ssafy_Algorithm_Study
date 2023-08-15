arr = [list(map(int, input().split())) for _ in range(19)]
# 우, 하, 우하, 우상
dr = [0,1,1,-1]
dc = [1,0,1,1]

def concave():
    for i in range(19):
        for j in range(19):
            # 0이면 스킵
            if arr[i][j]:
                # win은 1 또는 2
                win = arr[i][j]
                for d in range(4):
                    # i,j는 시작값 / r,c는 델타확인값
                    r, c = i, j
                    # 기본 바둑알 1개
                    cnt = 1
                    # 델타 이동하며 오목 확인
                    while True:
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < 19 and 0 <= nc < 19 and arr[nr][nc] == win:
                            r, c = nr, nc
                            cnt += 1
                        else: break
                    # 5개면 승리
                    if cnt == 5:
                        # 시작값 이전 좌표 확인하여 6목이면 빠꾸
                        if 0 <= i - dr[d] < 19 and 0 <= j - dc[d] < 19 and arr[i-dr[d]][j-dc[d]] == win:
                            continue
                        else:
                            return win, i+1, j+1
    return 0

ans = concave()
if ans:
    print(f'{ans[0]}\n{ans[1]} {ans[2]}')
else:
    print(0)


'''
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 1 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

'''