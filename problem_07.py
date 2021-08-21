# https://projecteuler.net/problem=7

TARGET = 10001

prime_numbers = []
current_number = 2

while len(prime_numbers) < TARGET:
    is_prime = True

    for divisor in range(current_number):
        if divisor <= 1:
            continue

        if current_number % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        prime_numbers.append(current_number) 

    current_number += 1

print(prime_numbers[-1])