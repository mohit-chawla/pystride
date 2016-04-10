from collections import defaultdict
n,m = map(int, raw_input().split())

d = defaultdict(list)

for i in range(n):
    d['A'].append(raw_input())

for j in range(m):
    d['B'].append(raw_input())


for k in d['B']:
    x = list() #for printing in a single line
    if d['A'].count(k) > 0:
        if d['A'].count(k) == 1:
            print(d['A'].index(k)+1)
        elif d['A'].count(k) > 1:
            l = list(d['A'])
            for m in range(0,len(l)):
                if l[m] == k:
                    x.append(str(m+1)) 
            print ' '.join(x)
            del x[:]
    else:
        print('-1')
    
    


