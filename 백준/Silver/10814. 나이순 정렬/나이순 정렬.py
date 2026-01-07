import sys
input = sys.stdin.readline

N = int(input())
li = [list(map(str, input().split())) for _ in range(N)]

# print(li)
so_li = sorted(li, key= lambda x : int(x[0]))

for i in so_li:
    print(*i)

# print(so_li)

# print('\n'.join(map(str, so_li)))
