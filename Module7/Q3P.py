# Jose Diaz 11/12/23
# Create our parameter to check our list to multiply them and get our answer
# Q3



def multiple_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
# have our result get the number when we multiply our list

theList = [5, 2, 7, -1]
result = multiple_list(theList)
print(f"When we multiply all the numbers in the list {theList} the result is : {result}")
