N, S = map(int, input().split())
bro = list(map(int, input().split()))

# 최대공약수 함수
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 술래와 동생들의 위치차이 값 저장
d = []
for i in bro:
    d += [S - i] if S > i else [i - S]
# d 원소들의 최대공약수 산정
d_gcd = d[0]
for j in range(1, N):
    d_gcd = gcd(d_gcd, d[j])

print(d_gcd)