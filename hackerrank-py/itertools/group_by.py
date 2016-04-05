from itertools import groupby

args = raw_input();

for key,group in groupby(args):
    print((len(list(group)), int(key)),end=" ")
