# https://projecteuler.net/problem=3

TARGET = 600851475143  

division = TARGET
prime_factor = 2

while division > 1:
    if division % prime_factor == 0:
        division = division / prime_factor
    else:
        prime_factor += 1

print(prime_factor)

