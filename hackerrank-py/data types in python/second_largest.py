#take length of list input
n = int(raw_input())

#initialize list
L = []

list1 = raw_input()
list_of_ints = map(int, list1.split())
list_of_ints.sort()

max_n = list_of_ints[len(list_of_ints)-1]

while list_of_ints[len(list_of_ints)-1] == max_n:
    list_of_ints.pop()


print(list_of_ints[len(list_of_ints)-1])
