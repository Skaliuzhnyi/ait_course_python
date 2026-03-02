""" 
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

n = 600851475143
factor = 2

while factor * factor <= n:
    if n % factor == 0:
        n //= factor
    else:
        factor += 1 if factor == 2 else 2
        
print(n)