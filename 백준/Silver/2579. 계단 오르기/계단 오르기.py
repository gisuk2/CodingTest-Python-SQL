# 아마 DP문제같음. 각 계단마다 최댓값 구하는게 좋을듯

import sys
input = sys.stdin.read

data = list(map(int,input().split()))

N = data[0]
stairs = [0] + data[1:]

dp = [0]*(N+3)

if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]


    for i in range(3,N+1):
        dp[i] = max((dp[i-2] + stairs[i]) , (dp[i-3] + stairs[i] + stairs[i-1]))

    print(dp[N])