import itertools
#take input word and length k
input_str = raw_input().split()

keyword = input_str[0]
keyword = sorted(keyword)
k = int(input_str[1])

L = list(itertools.permutations(keyword,k))

#print the formatted answer
for i in range(0,len(L)):
	print ''.join(L[i])
