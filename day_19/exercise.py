import csv
import json
from operator import itemgetter
import re

# # Execise 1


def get_num_of_newline(file_path):
    with open(file_path) as f:
        str_file = f.read().splitlines()
    return len(str_file)


def get_num_word(file_path):
    with open(file_path) as f:
        str_file = f.read()
    return len(str_file.split())


# 1
# -
print(get_num_of_newline(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/michelle_obama_speech.txt"))
print(get_num_word(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/michelle_obama_speech.txt"))

# -
print(get_num_of_newline(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/michelle_obama_speech.txt"))
print(get_num_word(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/michelle_obama_speech.txt"))

# -
print(get_num_of_newline(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/donald_speech.txt"))
print(get_num_word(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/donald_speech.txt"))

# -
print(get_num_of_newline(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/melina_trump_speech.txt"))
print(get_num_word(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/melina_trump_speech.txt"))

# 2


def most_spoken_languages(filename, top_n):
    f = open(filename, encoding="utf-8")
    countries = json.load(f)
    languages = []

    for country in countries:
        for languange in country["languages"]:
            languages.append(languange)

    language_counter = {}

    for languange in languages:
        if languange not in language_counter:
            language_counter[languange] = 0

        language_counter[languange] += 1

    return list(sorted(language_counter.items(),
                       key=lambda items: items[1], reverse=True))[:top_n]


print(most_spoken_languages(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/countries_data.json", 10))


def most_populated_countries(filename, top_n):
    f = open(filename, encoding="utf-8")
    countries = json.load(f)
    populations = []

    for country in countries:
        populations.append(
            {"country": country["name"], "population": country["population"]})

    return sorted(populations, key=itemgetter("population"), reverse=True)[:top_n]


print(most_populated_countries(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/countries_data.json", 10))

# Exercise 2
# 4


def get_email_address(filename):
    with open(filename) as f:
        str_file = f.read()

    match = re.findall(
        "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", str_file)

    return match


print(get_email_address(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/email_exchanges_big.txt"))

# 5


def find_most_common_words(filename, top_n):
    with open(filename) as f:
        words = f.read().split()

    common_words = {}

    for word in words:
        if word not in common_words:
            common_words[word] = 0
        common_words[word] += 1

    return sorted(common_words.items(), key=lambda items: items[1], reverse=True)[:top_n]


print(find_most_common_words(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/donald_speech.txt", 10))

# 6
print(find_most_common_words(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/obama_speech.txt", 10))

print(find_most_common_words(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/michelle_obama_speech.txt", 10))

print(find_most_common_words(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/melina_trump_speech.txt", 10))

# 7??

# 8
print("\n", find_most_common_words(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/romeo_and_juliet.txt", 10))

9

# a)


def count_num_line(filename):
    num_line = 0

    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=",")

        for _ in csv_reader:
            num_line += 1

    return num_line


print(count_num_line(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/hacker_news.csv"))

# b)


def count_num_line_contain_javascript(filename):
    num_line = 0
    languages = ["JavaScript", "javascript", "Javascript"]

    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=",")

        for row in csv_reader:
            txt = ", ".join(row[1:3])
            if languages[0] in txt or languages[1] in txt or languages[2] in txt:
                num_line += 1

    return num_line


print(count_num_line_contain_javascript(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/hacker_news.csv"))

# c


def count_num_line_contain_java(filename):
    num_line = 0

    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=",")

        for row in csv_reader:
            txt = ", ".join(row[1:3])
            if len(re.findall("[Java]{4}|[java]{4}", txt)):
                num_line += 1

    return num_line


print(count_num_line_contain_java(
    "D:/iseng-berhadiah/30_days_with_python/day_19/data/hacker_news.csv"))
