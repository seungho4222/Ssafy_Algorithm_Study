def solution(priorities, location):
    answer = 0
    # locatione 저장
    nums = list(enumerate(priorities))

    while True:
        check = nums.pop(0)
        # 큰 값 순 정렬
        for i in nums:
            if check[1] < i[1]:
                nums.append(check)
                break
        # 제일 큰값이면 프로그램 실행
        # 위치 맞을때 까지 반복
        else:
            answer += 1
            if check[0] == location:
                return answer



print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))