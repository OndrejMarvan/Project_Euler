# This function calculates the sum of even Fibonacci numbers up to a maximum value
def fibonacci_sum_even(max_value):
    # Start with the first two numbers in the Fibonacci sequence
    a = 1
    b = 2

    # Initialize the sum of even Fibonacci numbers to zero
    sum_even = 0

    # Loop until the current Fibonacci number exceeds the maximum value
    while a <= max_value:
        # Check if the current Fibonacci number 'a' is even
        if a % 2 == 0:
            # If it's even, add it to the sum
            sum_even += a

        # Update 'a' and 'b' to the next two numbers in the Fibonacci sequence
        # New 'a' is the old 'b', and new 'b' is the sum of old 'a' and 'b'
        a, b = b, a + b

    # Return the total sum of even Fibonacci numbers found
    return sum_even

# Use the function to find the sum of even Fibonacci numbers up to 4 million
result = fibonacci_sum_even(4000000)

# Print the result, formatted with commas for easier reading
print("{:,}".format(result))

