import datetime

# Today Date
today= datetime.date.today()
print(today.day) # 15
print(today.month) # 5
print(today.year) # 2023
print(today) # 2023-05-15

print(today.weekday()) # weekday Monday= 0 Sunday=6

print(today.isoweekday()) # weekday Monday= 1 Sunday=7

create_day = datetime.date(2020,6,9)
print(create_day) # 2020-06-09

new_year = datetime.date(2023,6,21) # 37 days left to Asmin's birthday party
days_remaining = new_year - today
print(days_remaining)

time = datetime.time(1,2,44,100)  # (01:02:44.000100) 1 hour 2 minute 44 seconds 100 miliseconds
print(time)

date_and_time = datetime.datetime(2023,1,22,12,44,12,1000) # 2023-01-22 12:44:12.001000
print(date_and_time)

#Move forward with time delta

time_delta = datetime.timedelta(days=10) #10 days after the 'date_and_time' 2023-02-01 12:44:12.001000
print(date_and_time+time_delta)

time_delta = datetime.timedelta(days=10) #10 days after the 'date_and_time' 2023-01-12 12:44:12.001000
print(date_and_time-time_delta)

#Convert a string to a date object
date_string = '2023-12-04'

date_object = datetime.date.fromisoformat(date_string)
print(date_object) # 2023-12-04

time_delta = datetime.timedelta(days=5)
print(date_object+time_delta) # 2023-12-09

today = datetime.date.today()
print(today)

birthday = datetime.date(2023,8,13)

days_to_bithday = birthday-today

print(days_to_bithday) # 90 days

After_20days = datetime.timedelta(days=20)
print((today+After_20days).isoweekday()) # 2023-06-04 7 => Sunday

today_string = '2020-12-04'

date_of_it = datetime.date.fromisoformat(today_string)

print(date_of_it) # 2020-12-04


