from math import radians
import numbers


# age = 23
# height = 165.0
# complex_number = 1 + 1j

# # 4
# base = float(input("Base: "))
# height = float(input("Height: "))
# area = 0.5 * base * height
# print("The area of the triangle is", area)

# # 5
# side_a = int(input("Side a: "))
# side_b = int(input("Side b: "))
# side_c = int(input("Side c: "))
# print("Perimeter of the triangle is", side_a + side_b + side_c)

# # 6
# length = float(input("Length: "))
# width = float(input("Width: "))
# area = length * width
# perimeter = 2 * (length + width)

# # 7
# radius = float(input("Radius: "))
# area = 3.14 * radius**2
# circumference = 2 * 3.14 * radius

# 8
# slope_1 = 2
# x_intercept = None
# y_intercept = -2

# # 9
# x_1, y_1 = 2, 2
# x_2, y_2 = 6, 10

# slope_2 = (y_2 - y_1) / (x_2 - x_1)
# euc_distance = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5

# # 10
# print(slope_1, slope_2)  # Same

# # 11
# x = -3
# y = x**2 + 6*x + 9
# print(y)

# # 12
# python_len = len("python")
# dragon_len = len("dragon")
# print(python_len != dragon_len)

# 13
# print("on" in "python")
# print("on" in "dragon")

# 14
# print("jargon" in "I hope this course is not full of jargon")

# 15
# print("on" not in "python")
# print("on" not in "dragon")

# 16
# print(str(float(len("python"))))

# 17 (Use modulus operator)
# number = 3
# print(number % 2 == 0)


# 18
print((7 // 3) == int(2.7))

# 19
print(type("10") == type(10))

# 20
# print(type(int('9.8')) == type(10))  # Value Error

# 21
# hours = int(input("Enter hours: "))
# rate = int(input("Rate per hour: "))
# print("Weekly earning is", hours * rate)

# 22
age = int(input("Enter number of years you have lived: "))
lived = age * 365 * 24 * 60 * 60
print("You have lived for", lived)

print("1 1 1 1 1", "2 1 2 4 8", "3 1 3 9 27", "4 1 4 16 64", "5 1 5 25 125", sep="\n")