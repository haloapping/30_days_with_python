# 1
string = ["Thirsty", "Days", "Of", "Python"]
print(" ".join(string))

# 2
string = ["Coding", "For", "All"]
print(" ".join(string))

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[:6])

# 10
print(company.index("Coding"))
print(company.find("Coding"))
print(company.rindex("Coding"))
print(company.rfind("Coding"))

# 11
company_replace = company.replace("Coding", "Python")
print(company_replace)

# 12
company_replace = company_replace.replace("Everyone", "All")
print(company_replace)

# 13
a = "Coding for All"
print(a.split())

# 14
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company.split(", "))

# 15
character = "C"

# 16
last_index = len("Coding For All") - 1
print(last_index)

# 17
print(a[10])

# 18

# 19

# 20
print(a.index("C"))

# 21
# print(a.index("F"))

# 22
print(a.rfind("l"))

# 23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because"))

# 24
print(sentence.rindex("because"))

# 25
print(sentence[sentence.index("because"):54])

# 26
print()

# 27
print()

# 28
print(a.startswith("Coding"))

# 29
print(a.endswith("coding"))

# 30
string = '   Coding For All      '
print(string.strip())

# 31
# 30DaysOfPython = "30DaysOfPython"
thirty_days_of_python = "thirty_days_of_python"

print(thirty_days_of_python.isidentifier())

# 32
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" ".join(libraries))

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# 35
radius = 10
area = 3.14 * radius**2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 36
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
