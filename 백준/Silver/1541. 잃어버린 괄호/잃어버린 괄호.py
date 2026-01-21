import sys
import re
from collections import deque

input = sys.stdin.readline

data = input().strip()

data_t = data.replace('-', '+')
li = list(map(int, data_t.split('+')))
# print(li)


cac = deque()
for i in data:
    if not re.match(r'\d', i):
        cac.append(i)
# print(cac)

total = li[0]
for i in li[1:]:
    if cac :
        if cac.popleft() == '-':
            # 이 뒤에 모든 기호를 마이너스로
            for k in range(len(cac)):
                cac[k] = '-'
            total -= i
            # print(total, i)
        else :
            total += i

print(total)
