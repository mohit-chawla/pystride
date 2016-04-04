from __future__ import division
n = int(raw_input())

d = dict()

def add_new_stu(name,p,c,m):
    d[name] = (float(p)+float(c)+float(m))/3

for i in range(0,n):
    this_stu = raw_input()
    this_stu_arr = this_stu.split()
    add_new_stu(this_stu_arr[0],this_stu_arr[1],this_stu_arr[2],this_stu_arr[3])

search_key = raw_input()

print(format(d[search_key],'.2f'))
