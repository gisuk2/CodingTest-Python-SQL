# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.


# 이것도 계수 비교로 풀어야 할 것 같은데

import sys
# input = sys.stdin.readline

S = input()
alp = 'abcdefghijklmnopqrstuvwxyz'

li = [-1]*26

for i in range(len(alp)):
    li[i] = S.find(alp[i])

print(*li)