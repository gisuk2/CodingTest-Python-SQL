import sys
N = int(sys.stdin.readline().strip())

words = set()
for _ in range(N):
    words.add(sys.stdin.readline().strip())

words = list(words)

# 정렬해야하는데 길이, 사전순
words.sort( key=lambda x: (len(x),x))

print('\n'.join(words))