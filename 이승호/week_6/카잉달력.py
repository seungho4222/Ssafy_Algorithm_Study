def lcm(x, y):
    def gcd(x,y):
        while y:
            x, y = y, x % y
        return x 
    return x * y // gcd(x,y)


T = int(input())
for tc in range(1, T+1):
    M, N, x, y = map(int, input().split())  # (M, N)은 마지막해, (x, y)는 찾아야 하는 해
    diff = abs(M-N)
    if x == y:
        print(x)
    elif M < N:
        a, b, k = 1, M+1, 1
        check = True
        while a != 1 and b != 1 + diff:
            b = b-diff
            k += M
            if abs(a-b) == abs(x-y):
                check = True
                break
        if check:
            k += x-1
            print(k)
    elif x < y:
        ...


    '''
      10 12
    1, 1
    1, 11
    1, 9
    1, 7
    1, 5
    1, 3
      13 11
    1, 1
    12,1
    10,1
    8,1
    6,1
    4,1
    2,1
    13,1
    11,1
    9,1
    7,1
    5,1
    3,1
      4, 7
    1,1
    1,5
    1,2
    1,6
    1,3
    1,7
    1,4
      5, 8
    1,1
    1,6
    1,3
    1,8
    1,5
    1,2
    1,7
    1,4
    '''