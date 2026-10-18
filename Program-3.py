# PROGRAM 3 – Program using user defined functions and lambdas.

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def check_even_odd(number):
    """Prints whether a number is even or odd."""
    if number % 2 == 0:
        return "{} is Even".format(number)
    else:
        return "{} is Odd".format(number)

square_num = lambda x: x ** 2

multiply_nums = lambda x, y: x * y

is_positive = lambda x: "Positive" if x > 0 else "Negative or Zero"

print("--- Testing User-Defined Functions ---")

sum_result = add_numbers(15, 25)

print("Result of add_numbers(15, 25): {}".format(sum_result))

even_odd_result = check_even_odd(7)

print("Result of check_even_odd(7): {}".format(even_odd_result))

print("\n--- Testing Lambda Functions ---")

print("Result of square_num(6): {}".format(square_num(6)))

print("Result of multiply_nums(4, 5): {}".format(multiply_nums(4, 5)))

print("Result of is_positive(-10): {}".format(is_positive(-10)))

print("\n--- Advanced Use Case: Lambda with map() ---")

numbers_list = [1, 2, 3, 4, 5]

doubled_list = list(map(lambda x: x * 2, numbers_list))

print("Original List: {}".format(numbers_list))

print("Doubled List: {}".format(doubled_list))
