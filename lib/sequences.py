#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0,1
    numbers = []
    for _ in range (length):
        
        numbers.append(a)
        a,b = b, a+b
    print(numbers,end ='\n')
        
print_fibonacci(2)