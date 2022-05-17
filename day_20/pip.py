import re
import requests

# 1


# def most_freq_word(url, top_n):
#     response = requests.get(url)
#     text = response.text
#     words = text.split()
#     count_words = {}

#     for word in words:
#         if word not in count_words:
#             count_words[word] = 0

#         count_words[word] += 1

#     return sorted(count_words.items(), key=lambda items: items[1], reverse=True)[:top_n]


# url = "http://www.gutenberg.org/files/1112/1112.txt"
# print(most_freq_word(url, 5))

# 2


def min_weight(url):
    response = requests.get(url)
    cats = response.json()
    weights = [cat["weight"]["metric"] for cat in cats]
    weights = [*[int(weight[0]) for weight in weights], *[int(weight[-1])
                                                          for weight in weights]]
    return min(weights)


url = "https://api.thecatapi.com/v1/breeds"


def max_weight(url):
    response = requests.get(url)
    cats = response.json()
    weights = [cat["weight"]["metric"] for cat in cats]
    weights = [*[int(weight[0]) for weight in weights], *[int(weight[-1])
                                                          for weight in weights]]
    return max(weights)


def mean_weight(url):
    response = requests.get(url)
    cats = response.json()
    weights = [cat["weight"]["metric"] for cat in cats]
    weights = [*[int(weight[0]) for weight in weights], *[int(weight[-1])
                                                          for weight in weights]]
    return sum(weights) / len(weights)


def median_weight(url):
    response = requests.get(url)
    cats = response.json()
    weights = [cat["weight"]["metric"] for cat in cats]
    weights = [*[int(weight[0]) for weight in weights], *[int(weight[-1])
                                                          for weight in weights]]
    sorted_weights = sorted(weights)

    if len(sorted_weights) % 2 != 0:
        return sorted_weights[(len(sorted_weights) // 2)]

    return (sorted_weights[(len(sorted_weights) // 2)] + sorted_weights[(len(sorted_weights) // 2) - 1]) / 2


def std_weight(url):
    response = requests.get(url)
    cats = response.json()
    weights = [cat["weight"]["metric"] for cat in cats]
    weights = [*[int(weight[0]) for weight in weights], *[int(weight[-1])
                                                          for weight in weights]]
    mean = sum(weights) / len(weights)
    diff = [(weight - mean)**2 for weight in weights]

    return sum(diff) / len(weights)


print(f"Min    : {min_weight(url):.2f}")
print(f"Max    : {max_weight(url):.2f}")
print(f"Mean   : {mean_weight(url):.2f}")
print(f"Median : {median_weight(url):.2f}")
print(f"Std    : {std_weight(url):.2f}")

# ii


def min_life_span(url):
    response = requests.get(url)
    cats = response.json()
    weights = ", ".join([cat["life_span"] for cat in cats])
    weights = [int(weight) for weight in re.findall("\d+", weights)]

    return min(weights)


url = "https://api.thecatapi.com/v1/breeds"


def max_life_span(url):
    response = requests.get(url)
    cats = response.json()
    weights = ", ".join([cat["life_span"] for cat in cats])
    weights = [int(weight) for weight in re.findall("\d+", weights)]

    return max(weights)


def mean_life_span(url):
    response = requests.get(url)
    cats = response.json()
    weights = ", ".join([cat["life_span"] for cat in cats])
    weights = [int(weight) for weight in re.findall("\d+", weights)]

    return sum(weights) / len(weights)


def median_life_span(url):
    response = requests.get(url)
    cats = response.json()
    weights = ", ".join([cat["life_span"] for cat in cats])
    weights = [int(weight) for weight in re.findall("\d+", weights)]
    sorted_weights = sorted(weights)

    if len(sorted_weights) % 2 != 0:
        return sorted_weights[(len(sorted_weights) // 2)]

    return (sorted_weights[(len(sorted_weights) // 2)] + sorted_weights[(len(sorted_weights) // 2) - 1]) / 2


def std_life_span(url):
    response = requests.get(url)
    cats = response.json()
    weights = ", ".join([cat["life_span"] for cat in cats])
    weights = [int(weight) for weight in re.findall("\d+", weights)]
    mean = sum(weights) / len(weights)
    diff = [(weight - mean)**2 for weight in weights]

    return sum(diff) / len(weights)


print(f"\nMin    : {min_life_span(url)}")
print(f"Max    : {max_life_span(url):.2f}")
print(f"Mean   : {mean_life_span(url):.2f}")
print(f"Median : {median_life_span(url):.2f}")
print(f"Std    : {std_life_span(url):.2f}")

# iii


def freq(url, name_count):
    response = requests.get(url)
    cats = response.json()
    items = [cat[name_count] for cat in cats]

    counts = {}

    for item in items:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1

    return counts


print("\n", freq(url, "name"))
print("\n", freq(url, "cfa_url"))
