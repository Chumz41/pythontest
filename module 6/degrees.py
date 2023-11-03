# Jose Diaz 11/2/2023
# problem number 5
# Print radians
# import our math module so we can use math.pi in our calculation
# Use the math module and formula to see the accuracy


import math

radians = float(input("Enter an angle in radians: "))

# get degrees from the radians
degrees = radians * (180 / math.pi)

# Use math module
degrees_from_math = math.degrees(radians)


print(f"{radians} radians is approximately {degrees:.2f} degrees (calculated).")
print(f"{radians} radians is exactly {degrees_from_math:.2f} degrees (math module).")
