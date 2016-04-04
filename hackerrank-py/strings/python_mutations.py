#mutations in python
#2possible methods

str = raw_input()
operation = raw_input()
op_arr = operation.split()
index = int(op_arr[0])
letter = op_arr[1]

final_str = str[:(index)] + letter + str[index+1:]
print(final_str)
