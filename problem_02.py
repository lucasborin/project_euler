# https://projecteuler.net/problem=2

LIMIT = 4000000

fibonacci = [0, 1]
term = fibonacci[-1]
sum = 0

while term <= LIMIT:
    next = fibonacci[-2] + fibonacci[-1]
    fibonacci.append( next )
    if next % 2 == 0:
        sum += next
    term = next

print(sum)