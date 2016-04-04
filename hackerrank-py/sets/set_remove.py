#set remove discard and pop operations
n = int(raw_input())

#initalise set
s = set();

#user input set items
set_items = map(int,raw_input().split());

#add elements to set
for j in range(0,len(set_items)):
	s.add(set_items[j])

#input number of commands
num_of_ops = int(raw_input())

#take commands from user
for i in range(0,num_of_ops):
	this_op = raw_input().split()
	op_to_do = this_op[0]
	if op_to_do == 'remove':
		op_index = int(this_op[1])
		s.remove(op_index)
	elif op_to_do == 'discard':
		op_index = int(this_op[1])
		s.discard(op_index)
	elif op_to_do == 'pop':
		s.pop()

#print final sum 
l = list(s)
answer = 0
for k in range(0,len(l)):
	answer += l[k]
print(answer)