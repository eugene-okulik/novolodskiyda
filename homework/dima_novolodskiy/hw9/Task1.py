import datetime


pepol_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(pepol_date, "%b %d, %Y - %H:%M:%S")
full_name_month = datetime.datetime.strftime(python_date, "%B")
print(full_name_month)
python_new = datetime.datetime.strftime(python_date, "%d.%m.%Y, %H:%M")
print(python_new)


import datetime


now = datetime.datetime.now()
print(now)
today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(today_midnight)
after_midnight = now - today_midnight
print(after_midnight.seconds)
print(after_midnight)
print(now + datetime.timedelta(days=10, hours=10))