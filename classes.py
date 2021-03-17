import csv


# ----- 1 -----
class Calculator:
    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


a = Calculator()

a.x = 9
a.y = 2

print(a.plus())
print(a.minus())
print(a.multiply())
print(a.divide())


# ----- 2 -----
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2

    def print_info(self):
        return f"Length: {self.length}, width: {self.width}, area: {self.area()}, perimeter: {self.perimeter()}."


my_rectangle = Rectangle(5, 9)

print(my_rectangle.area())
print(my_rectangle.perimeter())
print(my_rectangle.print_info())


# ----- 3 -----
class Employee:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def print__info(self):
        return f"Name: {self.name}, surname: {self.surname}, age: {self.age}, salary: {self.salary}"


with open('dataset1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    result = []
    for row in reader:
        new = Employee(row['name'], row['surname'], row['age'], row['salary'])
        print(new.print__info())
        result.append(new)

min_salary = min(result, key=lambda c: c.salary)
oldest_employee = max(result, key=lambda c: c.age)

print('')
print('-----------------Min salary--------------------')
print(min_salary.print__info())
print('')
print('-----------------Oldest employee--------------------')
print(oldest_employee.print__info())
