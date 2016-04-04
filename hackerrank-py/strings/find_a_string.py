#count the number of times a substring occurs in a string
#initialize
answer = 0

str = raw_input()
sub_str = raw_input()
len_sub_str = len(sub_str)

for i in range(len(str)):
    if str[i:i+len_sub_str] == sub_str:
        answer += 1

print(answer)
