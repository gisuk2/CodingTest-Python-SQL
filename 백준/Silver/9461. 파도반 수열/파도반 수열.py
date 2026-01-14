import sys
input = sys.stdin.read

data = list(map(int, input().split()))

T = data[0]
N_li = data[1:]

P = [0] * 101

P[0],P[1],P[2],P[3],P[4],P[5] = 0,1,1,1,2,2

for i in range(5,101):
    P[i] = P[i-1] + P[i-5]

for i in N_li:
    print(P[i])

