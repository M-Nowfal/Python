# PROGRAM 2 – Program to implement various types of actual arguments.

def my_function1(fname):
    print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

def my_function2(name):
    print("Hello", name)

my_function2("Emil")

def my_function3(fname, lname):
    print(fname + " " + lname)

my_function3("Emil", "Refsnes")

def my_function4(name="friend"):
    print("Hello", name)

my_function4("Emil")
my_function4("Tobias")
my_function4()
my_function4("Linus")

def my_function5(country="Norway"):
    print("I am from", country)

my_function5("Sweden")
my_function5("India")
my_function5()
my_function5("Brazil")
my_function5("Brazil")

def my_function6(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function6(animal="dog", name="Buddy")

def my_function7(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function7(name="Buddy", animal="dog")

def my_function8(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function8("dog", "Buddy")

def my_function9(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function9("dog", name="Buddy", age=5)

def my_function10(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function10(my_fruits)

def my_function11(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function11(my_person)

def my_function12(x, y):
    return x + y

result = my_function12(5, 3)
print(result)

def my_function13():
    return ["apple", "banana", "cherry"]

fruits = my_function13()

print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function14():
    return (10, 20)

x, y = my_function14()

print("x:", x)
print("y:", y)

def my_function15(name):
    print("Hello", name)

my_function15("Emil")

def my_function16(name):
    print("Hello", name)

my_function16(name="Emil")

def my_function17(a, b, c, d):
    return a + b + c + d

result = my_function17(5, 10, c=15, d=20)
print(result)
