# https://projecteuler.net/problem=6

RANGE_OF_NATURAL_NUMBERS = 100

sum_of_squares = 0
sum_of_range = 0

python_range = RANGE_OF_NATURAL_NUMBERS + 1

for natural_number in range(python_range):
    sum_of_squares += natural_number ** 2
    sum_of_range += natural_number

square_of_the_sum = sum_of_range ** 2
difference = square_of_the_sum - sum_of_squares

print(difference)