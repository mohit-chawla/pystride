
#num of english 
num_english = int(raw_input())
english = map(int,raw_input().split())

#num of french
num_french = int(raw_input())
french = map(int,raw_input().split())


F_set = set(french)

E_set = set(english)
u = E_set.difference(F_set)

print(len(u))