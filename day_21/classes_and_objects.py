# creating a class
import statistics
from collections import Counter


class Person:
    pass


print(Person())

# creating an object
person = Person()
print(person)

# constructor


class Person:
    def __init__(self, name):
        self.name = name


person = Person("Apping")
print(person.name)


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


person = Person("Alfiyanto", "Kondolele", 23, "Indonesia", "Luwu Timur")
print(person.firstname)
print(person.lastname)
print(person.age)
print(person.country)
print(person.city)

# object methods


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def personal_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. He live in {self.city}, {self.country}."


person = Person("Alfiyanto", "Kondolele", 23, "Indonesia", "Luwu Timur")
print(person.personal_info())

# object default methods


class Person:
    def __init__(self, firstname="Alfiyanto", lastname="Kondolele", age=23, country="Indonesia", city="Luwu Timur"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def personal_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. He live in {self.city}, {self.country}."


person = Person("Rahel", "Silitonga", 23, "Indonesia", "Riau")
print(person.personal_info())

# Method to Modify Class Default Values


class Person:
    def __init__(self, firstname="Alfiyanto", lastname="Kondolele", age=23, country="Indonesia", city="Luwu Timur"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def personal_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. He live in {self.city}, {self.country}."

    def add_skill(self, skill):
        self.skills.append(skill)


person = Person("Rahel", "Silitonga", 23, "Indonesia", "Riau")
print(person.personal_info())
person.add_skill("Masak")
print(person.skills)

# inheritance


class Student(Person):
    pass


student_1 = Student()
student_2 = Student()
print(student_1)
print(student_1.personal_info())
student_1.add_skill("Makan")
print(student_1.skills)

print(student_2)
print(student_2.personal_info())

# Overriding parent method


class Student(Person):
    def __init__(self, firstname="Alfiyanto", lastname="Kondolele", age=23, country="Indonesia", city="Luwu Timur", gender="Male"):
        super().__init__(firstname, lastname, age, country, city)
        self.gender = gender

    def personal_info(self):
        gender = "He" if self.gender == "Male" else "She"

        return f"{self.firstname} {self.lastname} is {self.age} years old. {gender} live in {self.city}, {self.country}."


student_1 = Student(gender="Female")
print(student_1.personal_info())

# Exercise
# 1


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        return statistics.mode(self.data)

    def std(self):
        return statistics.stdev(self.data)

    def variance(self):
        return statistics.variance(self.data)

    def freq_dist(self):
        return [(items[0], items[1]) for items in Counter(self.data).items()]

    def describe(self):
        print(f"Count     : {self.count()}")
        print(f"Sum       : {self.sum()}")
        print(f"Min       : {self.min()}")
        print(f"Max       : {self.max()}")
        print(f"Range     : {self.range()}")
        print(f"Mean      : {self.mean()}")
        print(f"Median    : {self.median()}")
        print(f"Mode      : {self.mode()}")
        print(f"Variance  : {self.variance()}")
        print(f"Std       : {self.std()}")
        print(f"Freq Dist : {self.freq_dist()}")


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print(data.describe())

# Exercise 2


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, income):
        self.incomes.append(income)

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_income(self):
        return sum(self.incomes)

    def total_expense(self):
        return sum(self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"Firstname : {self.firstname}\nLastname  : {self.lastname}\nIncomes   : {self.total_income()}\nExpenses  : {self.total_expense()}\nBalance   : {self.account_balance()}"


person = PersonAccount("Alfiyanto", "Kondolele")
person.add_income(12)
person.add_income(12)
person.add_expense(24)
print(person.account_info())
