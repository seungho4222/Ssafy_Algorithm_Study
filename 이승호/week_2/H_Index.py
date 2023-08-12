def solution(citations):
    answer = 0
    # 인용횟수 체크용 배열
    h_cite = max(citations)
    temp = [0] * (h_cite + 1)
    # 인용횟수 체크
    for i in citations:
        for j in range(0, i+1):
            temp[j] += 1
    # c회 이상 인용한 논문이 C권 인상인 경우 최대값
    for c in range(1, h_cite+1):
        if temp[c] >= c and answer < c:
            answer = c
    return answer


citations = [3,0,6,1,5]
print(solution(citations))