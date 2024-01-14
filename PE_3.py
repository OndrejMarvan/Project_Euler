#Problem 3: Largest Prime Factor. 
#The prime factors of 13195 are 5, 7, 13, and 29.
#What is the largest prime factor of the number 600851475143? 

import sympy as sp

# Define the number for which we want to find the largest prime factor
number = 600851475143

# Find the prime factors of the number
prime_factors = sp.primefactors(number)

# Get the largest prime factor
largest_prime_factor = max(prime_factors)
largest_prime_factor
