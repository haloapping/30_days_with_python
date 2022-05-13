# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [number for number in numbers if number > 0]
print(positive_numbers)

# 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [k for i in list_of_lists for j in i for k in j]
print(flat_list)

# 3
list_of_tuples = [(i, 1, (i**1), (i**2), (i**3), (i**4), (i**5))
                  for i in range(0, 11)]
print(list_of_tuples)

# 4
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[city[0].upper(), city[0][:3].upper(), city[-1].upper()]
             for country in countries for city in country]
print(countries)

# 5
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [{"country": city[0].upper(), "city": city[-1].upper()}
             for country in countries for city in country]
print(countries)

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
names = [firstname + " " +
         lastname for name in names for firstname, lastname in name]
print(names)

# 6


def slope(point_1, point_2):
    return (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])


print(slope((1, 1), (2, 2)))


def intercept(point, slope):
    return point[1] - (slope * point[0])


print(intercept((5, 4), 3/4))
