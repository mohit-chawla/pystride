n = int(raw_input())
nSet = raw_input()
nSet_int = map(int,nSet.split())
m = int(raw_input())
mSet = raw_input()
mSet_int = map(int,mSet.split())

set1 = set(nSet_int)
set2 = set(mSet_int)

L = []

d1 = set1.difference(set2)
d2 = set2.difference(set1)

L.extend(d1)
L.extend(d2)
L.sort()

for i in range(0,len(L)):
    print(L[i])
