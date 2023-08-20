def solution(n, edge):
    answer = 0
    # 인접리스트
    arr = [[] for _ in range(n+1)]
    for i in edge:
        arr[i[0]] += [i[1]]
        arr[i[1]] += [i[0]]
    # 시작점 스택, 방문기록 체크
    stack = [1]
    visited = [0] * (n+1)
    while stack:
        # temp: 중간 저장소
        temp = []
        # save: 출력값 저장용
        save = []
        while stack:
            t = stack.pop(0)
            visited[t] = 1
            for i in arr[t]:
                if not visited[i] and i not in stack and i not in temp:
                    temp += [i]
            save += [t]
        # 더 이상 노드 탐색 불가능할 경우 마지막 탐색 노드 수 출력
        if not temp:
            for _ in save:
                answer += 1
            return answer
        # 노드 탐색 가능 할 경우 스택 변경 후 탐색
        stack = temp

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))