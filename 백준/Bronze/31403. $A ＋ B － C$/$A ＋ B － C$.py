li_str=[]
for i in range(3):
    li_str.append(input())

answer_str = ''
answer_int = 0

answer_str = li_str[0] + li_str[1]
answer_str = int(answer_str) - int(li_str[2])
answer_int = int(li_str[0]) + int(li_str[1]) - int(li_str[2])


print(answer_int)
print(answer_str)
