# datetime
from datetime import datetime, date, time, timedelta

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

print(f"{day}-{month}-{year} {hour}:{minute}:{second}")

timestamp = now.timestamp()
print(timestamp)

# Formatting Date Output using strftime
new_year = datetime(2020, 1, 1)
print(new_year)
year = new_year.year
month = new_year.month
day = new_year.day
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(f"{day}-{month}-{year} {hour}:{minute}:{second}")

now = datetime.now()
time_1 = now.strftime("%H:%M:%S")
print(f"time: {time_1}")

time_2 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_2)

time_3 = now.strftime("%d/%m/%Y, %H:%M:%S")

# String to Time Using strptime
date_string = "31 December, 2019"
print(f"date_string: {date_string}")
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(f"date_object: {date_object}")

# using date from datetime
d = date(2020, 1, 1)
print(d)
print(f"Current date {d.today()}")
today = d.today()
print(f"Current year: {today.year}")
print(f"Current year: {today.month}")
print(f"Current year: {today.day}")

# using time from datetime
time_1 = time()
print(f"time_1: {time_1}")

time_2 = time(10, 30, 50)
print(f"time_2: {time_2}")

time_3 = time(10, 30, 50, 343535)
print(f"time_2: {time_3}")

# Difference between two points in time using
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print(f"Time left for new year: {time_left_for_newyear}")

datetime_1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
datetime_2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
print(f"Time left for new year: {datetime_2 - datetime_1}")

# Difference between two points in time using timedelta
time_1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
time_2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
print(time_1 - time_2)

# Exercise
# 1
today = datetime.now()
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
timestamp = today.timestamp()

print(f"Today     : {today}")
print(f"Day       : {day}")
print(f"Month     : {month}")
print(f"Year      : {year}")
print(f"Hour      : {hour}")
print(f"Minute    : {minute}")
print(f"Timestamp : {timestamp}")
print(datetime.fromtimestamp(timestamp), "\n")

# 2
current_date = today.strftime("%m/%d/%Y, %H:%M:%S")
print(current_date, "\n")

# 3
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_string)
print(date_object, "\n")

# 4
time_now = datetime.now()
time_new_year = datetime(year=2023, month=1, day=1,
                         hour=0, minute=0, second=0, microsecond=0)
diff = time_new_year - time_now
print(time_now)
print(time_new_year)
print(diff, "\n")

# 5
time_now = datetime.now()
time_unix = datetime(year=1970, month=1, day=1,
                     hour=0, minute=0, second=0, microsecond=0)
diff = time_now - time_unix
print(time_now)
print(time_unix)
print(diff)
