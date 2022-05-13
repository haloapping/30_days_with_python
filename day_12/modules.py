# Exercise 1

# 1
import random
import string


def random_user_id():
    chars = list(string.ascii_letters + string.digits + string.punctuation)
    user_id = []

    for _ in range(6):
        user_id.append(random.choice(chars))

    return "".join(user_id)


print(random_user_id())

# 2


def user_id_gen_by_user():
    len_id = int(input("Enter length id : "))
    num_id = int(input("Number of id    : "))

    chars = list(string.ascii_letters + string.digits + string.punctuation)
    user_id = []
    users_id = []

    for _ in range(num_id):
        for _ in range(len_id):
            user_id.append(random.choice(chars))
            user_id_str = "".join(user_id)

        users_id.append(user_id_str)
        user_id.clear()

    return users_id


print(user_id_gen_by_user())

# 3


def rgb_color_gen():
    rgb_color = []

    for _ in range(3):
        rgb_color.append(random.randint(0, 256))

    return f"rgb({rgb_color[0]}, {rgb_color[1]}, {rgb_color[2]})"


print(rgb_color_gen())


# Exercise 2
# 1
def list_of_hexa_colors():
    six_alphabet = string.ascii_lowercase[:6]
    digits = string.digits
    hexa_code = list(six_alphabet + digits)
    hexa = []

    for _ in range(6):
        hexa.append(random.choice(hexa_code))

    return "#" + "".join(hexa)


print(list_of_hexa_colors())


# 2
def generate_colors(code_name, num_color):
    colors = []

    for _ in range(num_color):
        if code_name == "rgb":
            colors.append(rgb_color_gen())
        else:
            colors.append(list_of_hexa_colors())

    return colors


print(generate_colors("rgb", 3))

# Exercise 3
# 1


def shuffle_list(items):
    random.shuffle(items)

    return items


items = [1, 2, 3, 4, 5]
print(shuffle_list(items))

# 2


def random_number():
    numbers = list(range(10))
    unique_number = []

    while len(unique_number) < 7:
        number = str(random.choice(numbers))

        if number not in unique_number:
            unique_number.append(number)

    return "".join(unique_number)


print(random_number())
