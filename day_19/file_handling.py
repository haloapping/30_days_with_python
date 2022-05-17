# Opening Files for Reading
import json
import os
f = open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt")
print(f, "\n")

# read()
f = open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt")
txt = f.read()
print(type(txt))
print(txt, "\n")
f.close()

# read() limit character
f = open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt")
txt = f.read(10)
print(type(txt))
print(txt, "\n")
f.close()

# readline()
f = open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt")
txt = f.readline()
print(type(txt))
print(txt, "\n")
f.close()

# readlines()
f = open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt")
txt = f.readlines()
print(type(txt))
print(txt, "\n")
f.close()

# splitlines()
f = open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt")
txt = f.read().splitlines()
print(type(txt))
print(txt, "\n")
f.close()

# keyword "with"
with open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt") as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines, '\n')

# Opening files for writing and updating
# append
with open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt", "a") as f:
    f.write("\nThis new line")

# write (overwrite)
with open("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt", "w") as f:
    f.write("This new text.")

# Deleting files
# os.remove("D:/iseng-berhadiah/30_days_with_python/day_19/file.txt")

# File types
# dictionary format
person_dict = {
    "name": "Apping",
    "country": "Indonesia",
    "city": "Luwu Timur",
    "skills": ["Makan", "Tidur", "Nonton Youtube"]
}

# json format
person_json = """{
    "name": "Apping",
    "country": "Indonesia",
    "city": "Luwu Timur",
    "skills": ["Makan", "Tidur", "Nonton Youtube"]
}"""

# JSON to dict
person_dict = json.loads(person_json)
print(type(person_dict))
print(person_dict)
print(person_dict["name"])

# dict to JSON
person_json = json.dumps(person_dict, indent=4)
print(type(person_json))
print(person_json)

# Saving dict as JSON file
with open("D:/iseng-berhadiah/30_days_with_python/day_19/dict_to_json.json", "w") as f:
    json.dump(person_dict, f, ensure_ascii=False, indent=4)
