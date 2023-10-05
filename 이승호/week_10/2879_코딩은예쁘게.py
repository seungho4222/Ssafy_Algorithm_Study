N = int(input())  # 줄의 개수
tap = list(map(int, input().split()))  # 모든 탭을 뉴탭과 같은 상태로 !!
new_tap = list(map(int, input().split()))

cnt = 0  # 편집 회수
for i in range(N):  # 앞에서부터 하나씩 확인
    while tap[i] != new_tap[i]:  # 뉴탭과 다르면
        s = i  # 계산용 인덱스 번호
        if tap[i] < new_tap[i]:  # 뉴탭이 더 크면
            while s < N and tap[s] < new_tap[s]:  # 반복하면서
                tap[s] += 1  # 탭 증가하고
                s += 1  # 다음 인덱스 확인해보자
        else:  # 뉴탭이 더 작은 경우, 이하동문
            while s < N and tap[s] > new_tap[s]:
                tap[s] -= 1
                s += 1
        cnt += 1  # 연속 탭 편집 후 회수 증가
print(cnt)
