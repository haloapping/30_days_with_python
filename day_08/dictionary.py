# 1
dog = {}
print(dog)

# 2
dog["name"] = "Pigoy"
dog["color"] = "Brown Black"
dog["legs"] = 4
dog["age"] = 2
print(dog)

# 3
student = {"first_name": "Alfiyanto",
           "last_name": "Kondolele",
           "gender": "Male",
           "age": 23,
           "marital_status": "Not Married",
           "skills": ["Eat", "Sleep"],
           "country": "Indonesia",
           "city": "Luwu Timur",
           "address": "Wawondula"}
print(student)

# 4
print(len(student))

# 5
print(student["skills"], type(student["skills"]))

# 6
student["skills"].extend(["Watch Youtube", "Listen Music"])
print(student["skills"])

# 7
print(student.keys())

# 8
print(student.values())

# 9
print(student.items())

# 10
student.popitem()
print(student)

# 11
student.pop("skills")
print(student)
