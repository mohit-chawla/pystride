n,m = map(int,raw_input().split())

arr = map(int,raw_input().split())
A = map(int,raw_input().split())
B = map(int,raw_input().split())
A_set = set(A)
B_set = set(B)
happiness = 0

for i in range(0,len(arr)):
    if arr[i] in A_set:
        happiness += 1
    if arr[i] in B_set:
        happiness -= 1
        
print(happiness)
