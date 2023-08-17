#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# Initialize an empty list to store the multiples of 3 or 5.
multiples = []

# Iterate through numbers from 1 to 999 (below 1000).
for num in range(1, 1000):
    # Check if the current number is divisible by 3 or 5 without leaving a remainder.
    if num % 3 == 0 or num % 5 == 0:
        # If divisible, add the number to the 'multiples' list.
        multiples.append(num)

# Checkpoint
print(multiples)

# Initialize a variable to store the sum of multiples.
multiples_sum = 0

# Iterate through each number in the 'multiples' list.
for num in multiples:
    # Add the current number to the sum.
    multiples_sum += num

# Print the sum of the multiples.
print("The sum of all the multiples of 3 or 5 below 1000 is:", multiples_sum)
