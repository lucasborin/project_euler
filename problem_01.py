# https://projecteuler.net/problem=1

sum = 0

for natural_number in range(1000):    
    if natural_number % 3 == 0 or natural_number % 5 == 0:
        sum += natural_number

print(sum)