def fibonacci_sum_even(max_value):
    a, b = 1, 2  # Starting values of the Fibonacci sequence
    sum_even = 0  # Initialize sum of even Fibonacci numbers

    while a <= max_value:
        if a % 2 == 0:  # Check if the number is even
            sum_even += a
        a, b = b, a + b  # Move to the next numbers in the sequence

    return sum_even

# Call the function and print the result
result = fibonacci_sum_even(4000000)
print("{:,}".format(result))
