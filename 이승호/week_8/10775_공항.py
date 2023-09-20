G = int(input())  # 게이트 수
P = int(input())  # 비행기 수
g = [int(input()) for _ in range(P)]  # 비행기별 도킹 가능 번호
parent = [i for i in range(G+1)]  # 도킹탐색 시작번호
cnt = 0  # 도킹 비행기 수

def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])  # 경로 압축
    return parent[x]

for i in g:
    tmp = find_set(i)  # 도킹 가능 번호 찾기
    if tmp == 0:  # 도킹번호가 0이면 도킹 불가
        break
    parent[tmp] = parent[tmp-1]  # 도킹탐색 시작번호 변경
    cnt += 1
    
print(cnt)
