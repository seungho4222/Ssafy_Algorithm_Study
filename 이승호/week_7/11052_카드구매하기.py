N = int(input())  # 구매하려는 카드 수
p = [0] + list(map(int, input().split()))  # 카드 가격
max_v = 0

def purchase(idx, total):
    global max_v
    if idx > N:
        return
    if idx == N:
        max_v = max(max_v, total)
        return
    
    for i in range(1, N+1):
        purchase(idx+i, total+p[i])

purchase(0,0)
print(max_v)