# https://projecteuler.net/problem=4

LIMIT = 1000

largest_palindrome = 0

for first_number in range(LIMIT):
    for second_number in range(LIMIT):
        product = first_number * second_number
        
        string = str(product)
        size = len(string)
        half = size // 2

        first_part = string[0:half]
        second_part = string[half:size]
        second_inverted = second_part[::-1]

        if first_part == second_inverted and product > largest_palindrome:
            largest_palindrome = product

print(largest_palindrome)



