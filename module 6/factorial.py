# Jose Diaz 11/2/2023
# problem number 6
# Print factorials
# import our math module so we can use in our calculation
# Use the math module and formula to see the accuracy
# get the input to use later in the formula



import math


number = int(input("Enter a integer: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i
# Above is the formula below is the math module
factorial_module = math.factorial(number)


print(f"The factorial of {number} is {factorial} ")
print(f"The factorial of {number} is {factorial_module} ")
