#lists in python

#iniitalize the list
L = []

def op_append(x):
    L.append(int(x))

def op_insert(i,x):
    L.insert(int(i),int(x))

def op_remove(x):
    L.remove(int(x))

def op_pop():
    L.pop()

def op_reverse():
    L.reverse()

def op_sort():
    L.sort()

def op_count():
    L.count()


#take the input iterator limit
n = int(raw_input())

for i in range(0,n):
    this_op = raw_input()
    this_op_arr = this_op.split()
    op_to_do = this_op_arr[0]
    if op_to_do == 'insert':
        op_insert(this_op_arr[1],this_op_arr[2])
    elif op_to_do == 'print':
        print(L)
    elif op_to_do == 'append':
        op_append(this_op_arr[1])
    elif op_to_do == 'sort':
        op_sort()
    elif op_to_do == 'reverse':
        op_reverse()
    elif op_to_do == 'pop':
        op_pop()
    elif op_to_do == 'remove':
        op_remove(this_op_arr[1])
    
        
    
        
    
