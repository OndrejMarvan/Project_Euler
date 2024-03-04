def is_palindrome(num):
    # This function checks if a number is a palindrome
    return str(num) == str(num)[::-1]

def largest_palindrome_product(n):
    # This function finds the largest palindrome made from the product of two n-digit numbers
    max_num = 10**n - 1  # Largest n-digit number
    min_num = 10**(n-1)  # Smallest n-digit number
    max_palindrome = 0
    factors = (0, 0)
    
    # We start from the largest possible product of two n-digit numbers and work our way down
    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if product <= max_palindrome:
                # Since the numbers are decreasing, if the product is less than the
                # current maximum palindrome, then there is no need to proceed further
                break
            if is_palindrome(product):
                max_palindrome = product
                factors = (i, j)
    
    return max_palindrome, factors

# Find the largest palindrome made from the product of two 3-digit numbers
largest_palindrome, factors = largest_palindrome_product(3)

# Print the result with a sentence
print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome}, "
      f"which is the product of the numbers {factors[0]} and {factors[1]}.")