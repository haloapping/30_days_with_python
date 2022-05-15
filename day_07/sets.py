# Exercise 1
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1
print(len(it_companies))

# 2
it_companies.add("Twitter")
print(it_companies)

# 3
it_companies.update(["Bukalapak", "Gojek", "Grab", "Tokopedia", "Shopee"])
print(it_companies)

# 4
it_companies.remove("Bukalapak")
print(it_companies)

# 5
# Remove return error if item not found, but discard return not error

# Exercise 2

# 1
print(A.union(B))

# 2
print(A.intersection(B))

# 3
print(A.issubset(B))

# 4
print(A.isdisjoint(B))

# 5
print(A.union(B))
print(B.union(A))

# 6
print(A.symmetric_difference(B))

# 7
del A, B
# print(A)
# print(B)

# Exercise 3
# 1
print(set(age), len(age), len(set(age)))

# 2
# String is collection of character
# list is collection (mutable) with index, can assign duplicate value, and mixed datatype
# tuple is collection like list, but not modified (immutable)
# set is collection unique value, unordered

# 3
sentence = set("I am a teacher and I love to inspire and teach people".split())
print(len(sentence))
