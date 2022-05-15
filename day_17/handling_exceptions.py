# Exception Handling
# 1
try:
    print(10 + "5")
except:
    print("Something went wrong")

# 2
try:
    name = input("Enter your name: ")
    year_born = input("Year you were born: ")
    age = 2022 - year_born
    print(f"You are {name}. And your age is {age}.")
except:
    print("Something went wrong.")

# 3
try:
    name = input("Enter your name: ")
    year_born = input("Year you were born: ")
    age = 2022 - year_born
    print(f"You are {name}. And your age is {age}.")
except TypeError:
    print("Type error occured.")
except ValueError:
    print("Value error occured.")
except ZeroDivisionError:
    print("Zero division error occured.")

# 4
try:
    name = input("Enter your name: ")
    year_born = input("Year you were born: ")
    age = 2022 - year_born
    print(f"You are {name}. And your age is {age}.")
except TypeError:
    print("Type error occured.")
except ValueError:
    print("Value error occured.")
except ZeroDivisionError:
    print("Zero division error occured.")
else:
    print("I usually run with the try block.")
finally:
    print("I always run.")

# 5
try:
    name = input("Enter your name: ")
    year_born = input("Year you were born: ")
    age = 2022 - year_born
    print(f"You are {name}. And your age is {age}.")
except Exception as e:
    print(e)

# Unpacking

# list


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


nums = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*nums))

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)  # Not work
print(numbers)

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)

# dictionary


def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} year old."


person = {"name": "Apping", "country": "Indonesia",
          "city": "Luwu Timur", "age": 23}

print(unpacking_person_info(**person))

# Packing


def sum_all(*args):
    s = 0
    for arg in args:
        s += arg

    return s


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))

# dict


def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

    return kwargs


print(packing_person_info(name="Apping",
      country="Indonesia", city="Luwu Timur", age=23))

# Spreading in Python
list_one = [1, 2, 3]
list_two = [4, 5, 6, 7]
lists = [0, *list_one, *list_two]
print(lists)

list_country_1 = ["Finland", "Sweden", "Norway"]
list_country_2 = ["Denmark", "Iceland"]
nordic_countries = [*list_country_1, * list_country_2]
print(nordic_countries)


# Enumerate
for index, country in enumerate(list_country_1):
    print(index, country)

# Zip
fruits = ["banana", "orange", "mango", "lemon", "lime"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruit_and_vege = [{"fruit": fruit, "vege": vegetable}
                  for fruit, vegetable in zip(fruits, vegetables)]
print(fruit_and_vege)

# Exercise
names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']

*nordic_countries, es, ru = names
print(nordic_countries)
print(es)
print(ru)
