#itertools cartesian product
import itertools
#input lists
A = map(int, raw_input().split())
B = map(int, raw_input().split())

#print cartesian product as list
L = list(itertools.product(A,B))
print' '.join(map(str,L))