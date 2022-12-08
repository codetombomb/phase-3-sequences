#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0,1])
    else:
        sequence = [0, 1]
        count = 0
        while len(sequence) < length:
            sequence.append(sequence[-1] + sequence[-2])
            count += 1
        print(sequence)
        

print(print_fibonacci(10))