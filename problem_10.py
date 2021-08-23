# https://projecteuler.net/problem=10
# NOT COMPLETED YET

TARGET = 2000000

current_number = 2
sum = 0

while current_number <= TARGET:
    is_prime = True

    for divisor in range(current_number):
        if divisor <= 1:
            continue

        if current_number % divisor == 0:
            is_prime = False
            break
    
    if is_prime:
        sum += current_number 

    current_number += 1

print(sum)