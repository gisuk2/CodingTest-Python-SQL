import sys
input = sys.stdin.readline

M = int(input().strip())
temp = []

li = set()

for i in range(M):
    temp = input().split()
    order = temp[0]
    
    if len(temp) > 1:
        num = int(temp[1])

    match order:
        case 'add':
            li.add(num)
        case 'check':
            print(1) if num in li else print(0)
        case 'remove':
            li.discard(num) # 값이 없어도 에러 발생 안 함
        case 'toggle':    
            li.discard(num) if num in li else li.add(num)
        case 'all':
            li = set(range(1, 21))
        case 'empty':
            li = set()


