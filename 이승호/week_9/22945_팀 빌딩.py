N = int(input())  # 개발자 수
ability = list(map(int, input().split()))  # 각 개발자의 능력치

max_v = 0  # 출력값인 팀 능력치 최댓값

start = 0  # 개발자 A (왼쪽부터)
end = N-1  # 개발자 B (오른쪽부터)
while start + 1 < end:  # 중간 개발자 수 줄여가며 값 비교
    max_v = max(max_v, (end - start - 1) * min(ability[start], ability[end]))
    if ability[start] < ability[end]:
        start += 1
    else:
        end -= 1

print(max_v)
