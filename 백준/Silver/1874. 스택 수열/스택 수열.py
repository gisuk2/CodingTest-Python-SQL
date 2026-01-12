# [Step 1] target이 나올 때까지 숫자를 스텍에 push
# [Step 2] 스택의 맨 위가 내가 찾던 그 숫자인가?
# [Step 3] 아니면 이 수열은 성립 불가!
import sys
data = sys.stdin.read().split()
n = int(data[0])
arr = list(map(int, data[1:]))

stack = []
ans = []
cur = 1
possible = True

for target in arr:
    while cur <= target:
        stack.append(cur)
        ans.append('+')
        cur += 1

    if stack[-1] == target:
        stack.pop()
        ans.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(ans))
else:
    print('NO')