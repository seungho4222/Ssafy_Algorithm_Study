# from collections import deque

# for i in range(1000,99,-1):
#     save = i
#     check = True
#     teil = i % 10
#     while i > 10:
#         i //=10
#         if i % 10 <= teil:
#             check = False
#             break
#         teil = i % 10
#     if check: tmp.append(save)
# tmp.sort()

def gumsa(num):
    while num > 9:
        t = num % 10
        num //= 10
        if num % 10 <= t:
            return False
    return True
        

N = int(input())

if N > 1022:
    print(-1)
else:
    x = 10
    check = N
    while check-10 > 0:
        tmp = x
        k = 0
        while True:
            teil = tmp % 10
            tmp //= 10
            if tmp % 10 > teil + 1:
                break
            else:
                x = tmp * (10 ** (k+1))
            k += 1
            if len(str(x)) - 1 == k:
                break
        x += 10 ** k
        if gumsa(x) == False: continue
        check -= 1


    if N < 11:
        print(N)
    else:
        print(x)
