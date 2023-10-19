from heapq import heappush, heappop

N, L = map(int, input().split())  # N개의 수의 길이 L

A = list(map(int, input().split()))  # N개 수의 배열

q = []
heappush(q, [A[0], 0])
print(A[0], end=' ')

for i in range(1, N):
    heappush(q, [A[i], i])
    while True:
        w, idx = heappop(q)
        if idx < i - L + 1:
            continue
        print(w, end=' ')
        heappush(q, [w, idx])
        break
