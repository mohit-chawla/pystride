#intro to sets
#botany plant problem

from __future__ import division

numPlants = int(raw_input())
plantHeights = map(int,raw_input().split())
numDistinctHeights = len(set(set(plantHeights)))

sumDistinctHeights = 0
distinctHeights= set(set(plantHeights))
distinctHeightsList = list(distinctHeights)

for i in range(0,numDistinctHeights):
    sumDistinctHeights += int(distinctHeightsList[i])

print format(sumDistinctHeights/numDistinctHeights,'.3f')

