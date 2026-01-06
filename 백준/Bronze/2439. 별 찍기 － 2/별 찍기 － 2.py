N = int(input())
answer = ''
for i in range(1,N+1):
    answer = ' '*(N-i) + '*'*i
    print(answer)