# PROGRAM 8 – Program to implement various types of Inheritance.

class Device(object):
    def power_on(self):
        return "Device is now ON."


class Laptop(Device):
    def boot_os(self):
        return "Booting operating system..."


class Camera(object):
    def take_photo(self):
        return "Photo captured successfully!"


class Phone(object):
    def make_call(self):
        return "Dialing contact..."


class Smartphone(Phone, Camera):
    def browse_internet(self):
        return "Opening web browser..."


class Vehicle(object):
    def move(self):
        return "Vehicle is moving."


class MotorizedVehicle(Vehicle):
    def start_engine(self):
        return "Engine started."


class Car(MotorizedVehicle):
    def drive(self):
        return "Car is cruising on the highway."


class Shape(object):
    def info(self):
        return "This is a geometric shape."


class Circle(Shape):
    def area_circle(self):
        return u"Calculating Circle Area: \u03c0 * r\u00b2"


class Square(Shape):
    def area_square(self):
        return u"Calculating Square Area: side\u00b2"


class Employee(object):
    def log_in(self):
        return "Employee logged in."


class Manager(Employee):
    def approve_leaves(self):
        return "Manager approved leave request."


class Developer(Employee):
    def write_code(self):
        return "Developer is writing Python code."


class TeamLead(Manager, Developer):
    def manage_team(self):
        return "TeamLead is organizing a sprint planning."


if __name__ == "__main__":

    print("--- 1. Single Inheritance ---")

    my_laptop = Laptop()

    print(my_laptop.power_on())
    print(my_laptop.boot_os())
    print("\n--- 2. Multiple Inheritance ---")

    my_phone = Smartphone()

    print(my_phone.make_call())
    print(my_phone.take_photo())
    print(my_phone.browse_internet())


    print("\n--- 3. Multilevel Inheritance ---")

    my_car = Car()

    print(my_car.move())
    print(my_car.start_engine())
    print(my_car.drive())

    print("\n--- 4. Hierarchical Inheritance ---")

    c = Circle()
    s = Square()

    print("Circle: {} -> {}".format(
        c.info(), c.area_circle()
    ))
    print("Square: {} -> {}".format(
        s.info(), s.area_square()
    ))

    print("\n--- 5. Hybrid Inheritance ---")

    lead = TeamLead()

    print(lead.log_in())
    print(lead.approve_leaves())
    print(lead.write_code())
    print(lead.manage_team())

    print("\n--- Method Resolution Order (MRO) for Hybrid Class ---")

    print([cls.__name__ for cls in TeamLead.__mro__])