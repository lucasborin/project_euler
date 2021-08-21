# https://projecteuler.net/problem=9

TARGET = 1000

for a in range(TARGET):
    for b in range(TARGET):
        for c in range(TARGET):    
            if a >= b or b >= c:
                continue 

            if a + b + c != 1000:
                continue
             
            if (a ** 2) + (b ** 2) == (c ** 2):
                product = a * b * c
                print(product)
                exit()
    
