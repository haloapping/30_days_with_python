# Exercise 1
# 1
empty_tuple = ()
print(empty_tuple)

# 2
sisters = ("Rahel", "Tabita")
brothers = ("Adil", "Fiki")
print(sisters)
print(brothers)

# 3
siblings = sisters + brothers
print(siblings)

# 4
print(len(siblings))

# 5
family_members = list(siblings)
family_members.append("Apping")
print(family_members)

# Exercise 2
# 1
a, *b = family_members
print(a, b)

# 2
fruits = ("strawberry", "melon")
vegetables = ("kangkung", "bayam")
animals = ("ikan", "sapi")
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)

# 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4
print(food_stuff_lt[len(food_stuff_lt) // 2])

# 5
a, b, c, *food_staff_lt = food_stuff_lt
print(a, b, c, food_staff_lt)

# 6
del food_stuff_tp
# print(food_stuff_tp)

# 6
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
