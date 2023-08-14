T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        field[c][r] = 1
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    ans = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:
                ans += 1
                field[r][c] = 0
                stack = []
                while True:
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1:
                            stack += [(r,c)]
                            field[nr][nc] = 0
                            r, c = nr, nc
                            break
                    else:
                        if stack:
                            r, c = stack.pop()
                        else:
                            break

    print(f'#{tc}', ans)



'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

'''