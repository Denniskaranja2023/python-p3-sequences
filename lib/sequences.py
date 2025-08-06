#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # Empty list for non-positive length
        return

    fibonacci_sequence = [0, 1]

    # Generate the sequence until it reaches the desired length
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    # If length is 1, slice the list to return only the first element
    print(fibonacci_sequence[:length])