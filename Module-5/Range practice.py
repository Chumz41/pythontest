# First we identify our range provided in the question
# We create the parameter
# we use the if else statements to craete the scenarious in the question of it being divided by x number
# First we check wether it is divisible by 3 and 5 not or.
# jose Diaz 27/23

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both")
    elif number % 3 == 0:
        print("Divisible by three")
    elif number % 5 == 0:
        print("Divisible by five")
    else:
        print(number)
