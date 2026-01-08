import sys

# 필수: 입력을 받는 속도를 비약적으로 높여줍니다.
input = sys.stdin.readline

stack = []
n_str = input().strip()
if not n_str: exit() # 입력이 비어있을 경우 대비
n = int(n_str)

for _ in range(n):
    # split()을 통해 명령(cmd)과 값(value)을 분리
    order = input().split()
    cmd = order[0]

    match cmd:
        case 'push':
            stack.append(order[1])
        case 'pop':
            print(stack.pop() if stack else -1)
        case 'size':
            print(len(stack))
        case 'empty':
            print(1 if not stack else 0)
        case 'top':
            print(stack[-1] if stack else -1)