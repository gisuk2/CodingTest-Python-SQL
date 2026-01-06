# 팩토리얼 코드
# 0이 아닌 숫자가 나오면 cnt+1

N=int(input())
res=1
ans=0
cnt = 0
li=[]


for i in range(1,N+1):
    res *=i

li = list(str(res))
rev_li = li[::-1]

for i in rev_li:
    if i != '0':
        break
    if i == '0':
        cnt += 1
        


print(cnt)