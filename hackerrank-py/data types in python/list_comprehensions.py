#take user input, dimensions of cuboid
x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

#initialize empty list
answers = []

#comprehend list
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                answers.append([i,j,k])

print(answers)
