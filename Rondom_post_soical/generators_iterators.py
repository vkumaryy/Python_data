def fibonacci(max_value):
    """
    Generate Fibonacci numbers up to a given maximum value using a generator.

    Args:
        max_value (int): The maximum value for the Fibonacci numbers to be generated.

    Yields:
        int: The next Fibonacci number in the sequence.

    Example Usage:
        fibonacci(1000)

    Code Analysis:
        Inputs:
        - max_value: an integer representing the maximum value for the Fibonacci numbers to be generated.

        Flow:
        1. Initialize variables `a` and `b` to 0 and 1 respectively.
        2. Enter a while loop that continues as long as `a` is less than the `max_value`.
        3. Yield the current value of `a`.
        4. Update `a` to the value of `b` and `b` to the sum of the previous values of `a` and `b`.
        5. Repeat steps 3-4 until `a` is no longer less than `max_value`.
        6. Print each yielded Fibonacci number.

        Outputs:
        - The Fibonacci numbers up to the `max_value` are printed.
    """
    a, b = 0, 1
    while a < max_value:
        yield a
        a, b = b, a + b

for number in fibonacci(1000):
    print(number)