import datetime
# print(dir(datetime))
# Getting datetime Information
from datetime import datetime,date
now = datetime.now()
day = now.day
month = now.month
year = now.year
minute = now.minute
second = now.second
hour = now.hour
print(f'{day}/{month}/{year}, {hour}:{second}')

# Formatting Date Output Using strftime
new_year = datetime(2020,1,1)
print(new_year)
day_1 = new_year.day
month_1 = new_year.month
year_1 = new_year.year
hour_1 = new_year.hour
minute_1 = new_year.minute
second = new_year.second
print(f"The date is: {day_1}-{month_1}-{year_1}")

# Formatting date time using strftime method
now_1 = datetime.now()
t = now.strftime("%H:%M:%S")
print("Current Time : ", t)
time_one = now_1.strftime("%m/%d/%Y, %H:%M:%S")
print('Time One', time_one)
time_two = now.strftime("%m/%Y/%d, %H:%M:%S")
print('Time Two', time_two)

# String to Time Using strptime
date_string = "5 December, 2019"
date_object  = datetime.strptime(date_string,"%d %B, %Y")
print(date_object)

# Using date from datetime
d = date(2020,1,1)
print(d)
today = d.today()
print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)

# Time Objects to Represent Time
from datetime import time
a = time()
print('a =', a)
b = time(10,30,20)
print("b =", b)
c = time(hour=10,minute=20,second=30)
print("c =", c)

# Difference Between Two Points in Time Using

today = date(year=2024,month=11,day=5)
new_year = date(year=2020,month=1,day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)
t1 = datetime(year=2024,month=5,day=27)
t2 = datetime(year=2044,month=5,day=27)
diff = t2 - t1
diff_year = t2.year - t1.year
print('Difference in years between the two dates:', diff_year)
print('Difference between two dates: ', diff)



#=============================================Excersise=======================================#

# ========================
# Get the current day, month, year, hour, minute and timestamp from datetime module
# ========================
now_2 = datetime.now()
current_day = now_2.day
current_month = now_2.month
current_year = now_2.year
current_hour = now_2.hour
current_minute = now_2.minute
timestamp = now_2.timestamp()
print("Day: ", current_day)
print("Month: ", current_month)
print("Year: ", current_year)
print("Hour: ", current_hour)
print("Minute: ", current_minute)
print("Timestamp: ", timestamp)
# ========================

# ========================
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# ========================
formatted_date = now_2.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted Date: ", formatted_date)

# ========================
# Today is 5 December, 2019. Change this time string to time.
# ========================
date_string_1 = "5 December, 2019"
date_object_1 = datetime.strptime(date_string_1, '%d %B, %Y')
print("Date Object: ", date_object_1)

# ========================
# Calculate the time difference between now and new year.
# ========================
today = date.today()
new_year = date(year=2024,month=1,day=1)
time_left_for_newyear = new_year - today
print("Time Left For New Year: ", time_left_for_newyear)

# ========================
# Calculate the time difference between 1 January 1970 and now.
# ========================
epoch = datetime(1970, 1, 1)
time_since_epoch = now_2 - epoch
print("Time Since Epoch: ", time_since_epoch)

# ========================
# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
# ========================

