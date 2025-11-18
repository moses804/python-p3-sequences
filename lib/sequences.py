# lib/sequences.py

def print_fibonacci(length):
    """
    Prints a list of Fibonacci numbers up to the given length.
    """
    if length <= 0:
        print([])
        return

    fib_sequence = [0, 1]  # Start with the first two Fibonacci numbers

    # Generate Fibonacci numbers until the list reaches the requested length
    while len(fib_sequence) < length:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    # Slice the list if length is 1 (to return [0])
    print(fib_sequence[:length])
