#calculate number of distinct stamps
n = int(raw_input())
stamps = set()
for i in range(n):
    stamps.add(raw_input())
    
distinctStamps = set(stamps)

print(len(distinctStamps))
