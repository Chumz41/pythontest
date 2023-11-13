# Jose Diaz 11/12/23
# Create our parameter to check our list to get no repeats in the new list
# Q4


# create parameter to check on our list

def unique(originalList):
    uniqueSet = []
    for num in originalList:
        if num not in uniqueSet:
            uniqueSet.append(num)
    return uniqueSet

# get only unique in our new list
originalList = [1, 3, 3, 3, 6, 2, 3, 5]
result = (originalList)
print(f"Original List: {originalList}")
print(f"List with only unique numbers: {result}")