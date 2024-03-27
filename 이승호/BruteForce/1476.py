# 최대 범위 15 28 19
E, S, M = map(int, input().split())

now = 1  # 현재 년도
e = s = m = 1  # 계산 초기값

while [e, s, m] != [E, S, M]:
  e += 1
  if e > 15 : e = 1
  s += 1
  if s > 28 : s = 1
  m += 1
  if m > 19 : m = 1
  now += 1

print(now)