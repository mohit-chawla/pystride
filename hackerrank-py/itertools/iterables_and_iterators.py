from __future__ import division
from itertools import combinations as c

#user input to list L
N = int(raw_input())
L = map(str, raw_input().split())
K = int(raw_input())
L2 = c(L, K)
L3 = list(L2)
count_a = 0 

for i in range(0,len(L3)):
	if L3[i].count('a') > 0:
		count_a +=1

print count_a/len(L3)
