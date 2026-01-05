# 문제
# 자연수 
# \(N\)과 정수 
# \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 
# \(N\)과 
# \(K\)가 주어진다. (1 ≤ 
# \(N\) ≤ 10, 0 ≤ 
# \(K\) ≤ 
# \(N\))


# 이항계수 구하기... nCr 구하기인데 했었는데

import sys
# import combinations
# from itertools import combinations
input = sys.stdin.readline

n,k = map(int, (input().split()))

def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

# n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))
