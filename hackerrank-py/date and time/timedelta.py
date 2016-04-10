#!/usr/bin/env python3

import datetime

#read input
def read_datetime():
    return datetime.datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')

def main():
    T = int(input()) #num of testcases
    for _ in range(T):
        t1 = read_datetime()
        t2 = read_datetime()
        
        print(int(abs(t1 - t2).total_seconds()))

#called as a standalone program
if __name__ == '__main__':
    main()
