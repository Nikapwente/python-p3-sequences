#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    fib_sequence = [0,1]
    if (length==0):
        print([])
    elif (length==1):
        print([0])
    elif (length ==2):
        print(fib_sequence)
    else:        
        for x in range(2,length):
            next_term = fib_sequence[x-1] + fib_sequence[x-2]
            fib_sequence.append(next_term)
        print(fib_sequence)