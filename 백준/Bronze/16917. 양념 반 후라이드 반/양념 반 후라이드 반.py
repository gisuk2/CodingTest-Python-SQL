import sys

input = sys.stdin.readline

A, B, C, X, Y = map(int, input().split())
total=0
if A + B <= 2 * C:
    print(A * X + B * Y)
else:
    common = min(X,Y)
    total = common * 2 * C

    X -= common
    Y -= common

    if X > 0:
        total += min(X*A, X*2*C)
    if Y > 0:
        total += min(Y*B, Y*2*C)

    print(total)