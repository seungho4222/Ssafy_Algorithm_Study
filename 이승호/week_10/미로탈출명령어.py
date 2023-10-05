import sys
sys.setrecursionlimit(10**4)
                

def solution(n, m, x, y, r, c, k):
    global answer
    # d, l, r, u 사전 순
    dd = {0:'d', 1:'l', 2:'r', 3:'u'}
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    answer = ''

    arr = [[0]*(m+2)]
    for _ in range(n):
        arr.append([0]+['.']*m+[0])
    arr.append([0]*(m+2))
    
    min_move = abs(r-x) + abs(c-y)
    if min_move > k or (k - min_move)%2 == 1:
        return 'impossible'

    def maze(idx, a, b, st):
        global answer
        if k < idx + abs(a - r) + abs(b - c):
            return
        
        if idx == k and a == r and b == c:
            answer = st
            return
        
        for j in range(4):
            nr, nc = a + di[j], b + dj[j]
            if arr[nr][nc] == 0:
                continue
            elif not answer:
                maze(idx+1, nr, nc, st + dd[j])

    maze(0,x,y,'')
    return answer


print(solution(2,2,1,1,2,2,2))

'''
import sys
sys.setrecursionlimit(10**4)

dx = (1, 0, 0, -1)  # dlru 순서
dy = (0, -1, 1, 0)
ds = ('d', 'l', 'r', 'u')    
answer = ''

def dfs(x, y, string, move, n, m, r, c, k):
        global answer
        # 남은 횟수 안에 도착지까지 갈 수 없는 경우 stop
        if k < move + abs(x - r) + abs(y - c):
            return
            
        # 정답을 찾은 경우
        if move == k and x == r and y == c:
            answer = string
            return 
        
        # 사전 순으로 탐색
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0 < nx <= n and 0 < ny <= m and not answer:
                dfs(nx, ny, string[:]+ds[i], move+1, n, m, r, c, k)
                
def solution(n, m, x, y, r, c, k):
    
    min_move = abs(r-x)+abs(c-y)	# 도착지까지의 최소 이동 횟수
    # 최소 이동 횟수가 k보다 많거나,
    # 최소 이동 횟수 제외한 이동 횟수가 홀 수인 경우에는 도착지에 도착 불가능
    if min_move > k or (k - min_move) % 2 == 1:
        return "impossible"
    
    dfs(x, y, "", 0, n, m, r, c, k)
    return answer


from collections import deque

def solution(n, m, x, y, r, c, k):
    dx = (-1, 0, 0, 1)  # urld 순서
    dy = (0, 1, -1, 0)
    ds = ('u', 'r', 'l', 'd')    
    answer = ""
    
    total_move = abs(r-x)+abs(c-y)
    if total_move > k or (k - total_move) % 2 == 1:
        return "impossible"
    
    q = deque([(x, y, "", 0)])

    while q:
        x, y, string, move = q.pop()
        
        if move == k and x == r and y == c :
            return string
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0 < nx <= n and 0 < ny <= m and k >= move + abs(r-x) + abs(c-y) :
                q.append((nx, ny, string+ds[i], move+1))

    return answer
'''