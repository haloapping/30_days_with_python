import re

# match
txt = "I love to teach python and javascript"
match = re.match("I love to teach", txt, re.IGNORECASE)
print(match)
print(match.span())

start, end = match.span()
print(txt[start:end])

# search
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search("first", txt, re.IGNORECASE)
print(match.span())
start, end = match.span()
print("\n", txt[start:end])

# findall
match = re.findall("language", txt, re.IGNORECASE)
print("\n", match)

match = re.findall("Python|python", txt)
print(match)

match = re.findall("[Pp]ython", txt)
print(match)

# replace
match_replaced = re.sub("Python|python", "JavaScript", txt, re.IGNORECASE)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
print(txt)
remove_percent = re.sub('%', "", txt)
print(remove_percent)

# split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split("\n", txt))

# regex pattern
regex_pattern = r"apple"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
match = re.findall(regex_pattern, txt)
print(match)

match = re.findall(regex_pattern, txt, re.IGNORECASE)
print(match, "\n")

regex_pattern = r"[Aa]pple"
match = re.findall(regex_pattern, txt)
print(match)

# square bracket
regex_pattern = r"[Aa]pple"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
match = re.findall(regex_pattern, txt)
print(match)

regex_pattern = r"[Aa]pple|[Bb]anana"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
match = re.findall(regex_pattern, txt)
print(match)

# Escape character "\"
regex_pattern = r"\d"
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
match = re.findall(regex_pattern, txt)
print(match)

regex_pattern = r"\d+"
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
match = re.findall(regex_pattern, txt)
print(match)

# period "."
regex_pattern = r"[a]."
txt = '''Apple and banana are fruits'''
match = re.findall(regex_pattern, txt)
print(match)

regex_pattern = r"[a].*"
txt = '''Apple and banana are fruits'''
match = re.findall(regex_pattern, txt)
print(match)

# Zero or one time(?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r"[Ee]-?mail"
match = re.findall(regex_pattern, txt)
print(match)

# Quantifier in RegEx
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r"\d{4}"
match = re.findall(regex_pattern, txt)
print(match)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

# cart ^
# start with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r"^This"
match = re.findall(regex_pattern, txt)
print(match)

# negation
regex_pattern = r"[^A-Za-z ]+"
match = re.findall(regex_pattern, txt)
print(match)

# Exercise
# 1 : love : 6

# 2
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points = sorted([int(point) for point in points])
distance = sorted_points[-1] - sorted_points[0]
print(distance)

# Exercise 2
regex_pattern = r"\d|-"
txt = "firstname1"
match = re.findall(regex_pattern, txt, re.IGNORECASE)
print(match, "\n")
if len(match) == 0:
    print(True)
else:
    print(False)

# Exercise 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
regex_pattern = r"$|%|@|&|#|!|;|,"
clean_sentence = re.sub(regex_pattern, "", sentence, count=0)
print(clean_sentence)
