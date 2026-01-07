import sys
input = sys.stdin.readline

N = int(input())
li=[]
for i in range(N):
    li.append(list(map(int, input().split())))

# print(li)

# li[i][0] 값 i=0부터 끝까지 정렬, 2순위로 li[i][1] 순으로 정렬 
li.sort(key=lambda x : (x[1],x[0]))

for a,b in li:
    print(f"{a} {b}")
# print(li)