# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

RANGE = 20

smallest_number = 0
current_number = 0

while smallest_number == 0:
    can_devide = True
    
    for divisor in range(RANGE):
        if divisor == 0:
            continue

        if current_number % divisor != 0:
            can_devide = False
            break
    
    if can_devide:
        smallest_number = current_number
        
    current_number += 1

print(smallest_number)

