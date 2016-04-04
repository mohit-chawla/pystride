tup = ()

n = int(raw_input())
numbers = raw_input()
numbers_arr = numbers.split()

for i in range(0,n):
    tup += (int(numbers_arr[i]),)

print(hash(tup))
