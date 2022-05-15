# Exrecise 1
# 1
from base64 import b16decode
from operator import le
from turtle import back


empty_list = []
print(empty_list)

# 2
items = [1, 2, 3, 4, 5, 6, 7]
print(items)

# 3
print(len(items))

# 4
print(items[0], items[3], items[-1])

# 5
mixed_data_types = ["Apping", 23, 165, "Not Married", "Indonesia"]
print(mixed_data_types)

# 6
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# 10
it_companies[0] = "VALE"
print(it_companies)

# 11
it_companies.append("Tokopedia")
print(it_companies)

# 12
it_companies.insert(len(it_companies) // 2, "Bukalapak")
print(it_companies)

# 13
it_companies[-1] = it_companies[-1].upper()

print(it_companies)

# 14
print("#; ".join(it_companies))

# 15
print("Gojek" in it_companies)
print("Bukalapak" in it_companies)

# 16
it_companies.sort()
print(it_companies)

# 17
it_companies.sort(reverse=True)
print(it_companies)

# 18
print(it_companies[:3])

# 19
print(it_companies[-3:])

# 20
print(it_companies[len(it_companies) // 2])

# 21
it_companies.pop(0)
print(it_companies)

# 22
it_companies.pop(len(it_companies) // 2)
print(it_companies)

# 23
it_companies.pop()
print(it_companies)

# 24
it_companies.clear()
print(it_companies)

# 25
# del it_companies
# print(it_companies)

# 26
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
print(front_end + back_end)
front_end.extend(back_end)
print(front_end)

# 27
full_stack = front_end.copy()
print(full_stack)
full_stack.insert(full_stack.index("Redux") + 1, "Python")
print(full_stack)
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)

# Exercise 2
# 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
asc_ages = sorted(ages)
min_value, max_value = asc_ages[0], asc_ages[-1]
print(min_value, max_value)
asc_ages.append(min_value)
asc_ages.append(max_value)
print(asc_ages)
print(sum([asc_ages[len(asc_ages) // 2], asc_ages[len(asc_ages) // 2 + 1]]) / 2)
print(sum(asc_ages) / len(asc_ages))
print(max(asc_ages) - min(asc_ages))
average = sum(asc_ages) / len(asc_ages)
print(abs(min(asc_ages) - average))
print(abs(max(asc_ages) - average))
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombi',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

print(len(countries))

print(len(countries) // 2)
print(countries[len(countries) // 2])
a, b = countries[:len(countries) // 2], countries[len(countries) // 2:]
print(a, b)

other_countries = ['China', 'Russia', 'USA',
                   'Finland', 'Sweden', 'Norway', 'Denmark']
a, b, c, *d = other_countries
print(a, b, c, d)
