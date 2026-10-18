#  PROGRAM 5 – Program to implement a dictionary.

student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"],
    "gpa": 3.8
}

print("Initial Dictionary:")

print(student)

print("Total entries (length): {}\n".format(len(student)))


print("--- Reading Data ---")

print("Student Name: {}".format(student['name']))

email = student.get("email", "Email not provided")

print("Student Email: {}".format(email))

if "gpa" in student:
    print("GPA exists and is: {}\n".format(student['gpa']))


print("--- Updating & Adding Data ---")

student["age"] = 21

student["email"] = "alice@university.edu"

student.update({"gpa": 3.9, "status": "Active"})

print("Updated Dictionary:")

print(student, "\n")


print("--- Iterating Through Dictionary ---")

print("All Key-Value pairs:")

for key, value in student.items():
    print(" {}: {}".format(key, value))

print("\nJust the keys:")

for key in student.keys():
    print(" Key: {}".format(key))

print("\nJust the values:")

for val in student.values():
    print(" Value: {}\n".format(val))


print("--- Deleting Data ---")

removed_age = student.pop("age")

print("Removed age: {}".format(removed_age))

del student["status"]

last_item = student.popitem()

print("Removed last item: {}".format(last_item))

print("\nDictionary after deletions:")

print(student)

student.clear()

print("\nDictionary after clear():")

print(student)