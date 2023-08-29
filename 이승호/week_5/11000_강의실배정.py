import sys
input = sys.stdin.readline

N = int(input())  # 수업 수
tt = sorted([list(map(int, input().split())) for _ in range(N)])  # 시간표
visited = [0] * N
for i in range(N):  # 시간표 순회
    for j in range(N):
        if tt[i][0] >= visited[j]:
            visited[j] = tt[i][1]
            break
cnt = 0
for v in visited:
    if v: cnt += 1
print(cnt)
