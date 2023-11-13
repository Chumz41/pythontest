# Jose Diaz 11/12/23
# Create our parameter and define the range we want it to check from the integer
# Q2




def checkRange(number):
    if 1 <= number <= 10:
        print(f"{number} is in the range (1, 10)")
    else:
        print(f"{number} is not in the range (1, 10)")

# Test it to see if it out puts correctly using different numbers
ourNumber = int(input("pick a number >> "))
checkRange(ourNumber)