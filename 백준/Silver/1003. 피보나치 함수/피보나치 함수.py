import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

T= int(input_data[0])
test_cases = list(map(int, input_data[1:]))

zero_count = [0]*41
one_count = [0]*41

zero_count[0], one_count[0] = 1,0
zero_count[1], one_count[1] = 0,1

for i in range(2,41):
    zero_count[i] = zero_count[i-1] + zero_count[i-2]
    one_count[i] = one_count[i-1] + one_count[i-2]

results = []
for n in test_cases:
    results.append(f"{zero_count[n]} {one_count[n]}")

print('\n'.join(results))