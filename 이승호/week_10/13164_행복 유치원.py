N, K = map(int, input().split())  # N: 원생 수, K: 나누려는 조의 수
arr = list(map(int, input().split()))  # 원생들의 키, 오름차순 !!

tmp = []
for i in range(N-1):
    a = arr[i+1] - arr[i]  # 원생들의 키 차이 구하기
    tmp.append(a)
tmp.sort()  # 정렬

ans = 0
for j in range(N-K):  # N을 K로 나누었다 => N-K 까지 키 차이 더하기
    ans += tmp[j]

print(ans)