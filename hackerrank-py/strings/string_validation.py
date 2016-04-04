#string validation in python

#user input
input_str = raw_input()


for i in range(len(input_str)):
    if input_str[i].isalnum() == True:
        print "True"
        break
    if i == len(input_str)-1:
        print "False"

for i in range(len(input_str)):
    if input_str[i].isalpha() == True:
        print "True"
        break
    if i == len(input_str)-1:
        print "False"

        
for i in range(len(input_str)):
    if input_str[i].isdigit() == True:
        print "True"
        break
    if i == len(input_str)-1:
        print "False"

for i in range(len(input_str)):
    if input_str[i].islower() == True:
        print "True"
        break
    if i == len(input_str)-1:
        print "False"

for i in range(len(input_str)):
    if input_str[i].isupper() == True:
        print "True"
        break
    if i == len(input_str)-1:
        print "False"

