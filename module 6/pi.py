# Jose Diaz 11/2/2023
# problem number 4
# Print Pi in as close as possible
# Wiki how helped me figure out how to do step by step the nilakantha method on python
#Then used the math module to do it






from decimal import *
getcontext().prec = 100

def nilakantha(reps):
        result = Decimal(3.0)
        op = 1
        n = 2
        for n in range(2, 2*reps+1, 2):
                result += 4/Decimal(n*(n+1)*(n+2)*op)
                op *= -1
        return result

print("How many repetitions?")
repetitions = int(input())
print(nilakantha(repetitions))


import math


print("value of pi is: ", math.pi)