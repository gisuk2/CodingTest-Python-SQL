import sys
input = sys.stdin.readline

N = int(input().strip())

li = list(map(int, input().split()))
li.sort(reverse=False)

# print(li)
total = 0
ans = 0
for i in li:
    total += i
    ans += total
    
print(ans)
