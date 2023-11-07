def add_numbers(num1, num2):
    result = num1 + num2
    return result

sum_result = add_numbers(5,3)
print(sum_result)

def square(num):
    result = num**2
    return result

square_result = square(4)
print(square_result)

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print( i )

i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print(i)

def hello():
    print("Hello from module1")
if __name__ == "__main__":
    print("Executing module1 directly")
    hello()
else:
    print("module1 imported")