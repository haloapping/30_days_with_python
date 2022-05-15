# Exercise 1

# 1
# age = int(input("Enter your age: "))

# if age > 18:
#     print("You are old enough to learn to drive.")
# else:
#     print(f"You need {18 - age} more years to learn to drive")

# 2
# season = input("Month: ")

# if season in ["September", "October", "November"]:
#     print("Autumn")
# elif season in ["December", "January", "February"]:
#     print("Winter")
# elif season in ["March", "April", "May"]:
#     print("Spring")
# else:
#     print("Summer")

# 3
fruit = "banana"
fruits = ["banana", "orange", "mango", "lemon"]

if fruit in fruits:
    print("That fruit already exist in the list")
else:
    print("That fruit doesn't exist in the list")

# Exercise 3

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ["React", "MongoDB", "Node"],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person:
    print(person["skills"][len(person["skills"]) // 2])

if "skills" in person:
    if "Python" in person["skills"]:
        print(person["skills"])

if "JavaScript" in person["skills"] and "React" in person["skills"] and (len(person["skills"]) == 2):
    print("He is a frontend developer")
elif "Node" in person["skills"] and "MongoDB" in person["skills"] and "Python" in person["skills"] and (len(person["skills"]) == 3):
    print("He is a backend developer")
elif "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"] and (len(person["skills"]) == 3):
    print("He is a fullstack developer")
else:
    print("Unknown title")

if person["is_married"]:
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
