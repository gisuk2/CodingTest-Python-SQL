import sys
input = sys.stdin.readline

N,M = map(int, input().split())

name_to_id = {}
id_to_name = [""] * (N+1)

for i in range(1, N+1):
    name = input().strip()
    name_to_id[name] = i
    id_to_name[i] = name

for _ in range(M):
    query = input().strip()

    if query.isdigit():
        print(id_to_name[int(query)])
    else:
        print(name_to_id[query])
