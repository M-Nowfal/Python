# PROGRAM 4 – Program to demonstrate the use of lists, tuples and its related functions.

print("--- 1. Python Lists Demonstration ---")

fruits = ["apple", "banana", "cherry"]

print("Original list: {}".format(fruits))

fruits[1] = "blueberry"

print("After modifying index 1: {}".format(fruits))

fruits.append("orange")

print("After append(): {}".format(fruits))

fruits.insert(1, "mango")

print("After insert(1): {}".format(fruits))

fruits.remove("cherry")

print("After remove('cherry'): {}".format(fruits))

popped_item = fruits.pop()

print("After pop(): {} (Popped item: {})".format(fruits, popped_item))

fruits.reverse()

print("After reverse(): {}".format(fruits))

fruits.sort()

print("After sort(): {}".format(fruits))

print("\n--- 2. Python Tuples Demonstration ---")

coordinates = (10, 20, 30, 20)

print("Original tuple: {}".format(coordinates))

print("Note: Attempting to modify a tuple (e.g., coordinates[0] = 5) will raise a TypeError.")

occurences = coordinates.count(20)

print("Occurrences of 20: {}".format(occurences))

first_index = coordinates.index(30)

print("First index of 30: {}".format(first_index))

x, y, z, w = coordinates

print("Unpacked values: x={}, y={}, z={}, w={}".format(x, y, z, w))

print("\n--- 3. Functions Shared By Both ---")

numbers_list = [5, 2, 9, 1]

numbers_tuple = (5, 2, 9, 1)

print("Length -> List: {}, Tuple: {}".format(
    len(numbers_list), len(numbers_tuple)))

print("Max value -> List: {}, Tuple: {}".format(
    max(numbers_list), max(numbers_tuple)))

print("Min value -> List: {}, Tuple: {}".format(
    min(numbers_list), min(numbers_tuple)))

print("Sum total -> List: {}, Tuple: {}".format(
    sum(numbers_list), sum(numbers_tuple)))

print("sorted() function on Tuple: {}".format(
    sorted(numbers_tuple)))

print("\n--- 4. Data Type Conversion ---")

converted_tuple = tuple(numbers_list)

print("List converted to Tuple: {} | Type: {}".format(
    converted_tuple, type(converted_tuple)))

converted_list = list(numbers_tuple)

print("Tuple converted to List: {} | Type: {}".format(
    converted_list, type(converted_list)))
