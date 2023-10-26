# Function without Parameters
def add_two_numbers():
    first_number = 4
    second_number = -3
    print(first_number + second_number)
add_two_numbers()

# Function Returning a Value - Part 1
def add_two_numbers_1():
    first_number = 4
    second_number = -3
    return first_number + second_number
add_two_numbers_1()

# Function with Parameters
def add_two_numbers_2(first_number,second_number):
    return  first_number + second_number
add_two_numbers_2(2,3)

# Passing Arguments with Key and Value
def add_two_numbers_3(first_number,second_number):
    return  first_number + second_number
add_two_numbers_3(first_number=2,second_number=3)

# Function Returning a Value - Part 2
def find_even_num(n):
    even=[]
    for i in range(n + 1):
        if n % 2 == 0:
            even.append(i)
    return even

print(find_even_num(10))

# Function with Default Parameters
def add_two_numbers_4(first_number = 4,second_number = 3):
    return  first_number + second_number
print(add_two_numbers_4())

def add_two_numbers_5(first_number = 4,second_number = 3):
    return  first_number + second_number
print(add_two_numbers_5(5,3))

# Arbitrary Number of Arguments(If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.)
def add_two_numbers_6(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total

print(add_two_numbers_6(2,3,5))