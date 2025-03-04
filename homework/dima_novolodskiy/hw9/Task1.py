import datetime


pepol_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(pepol_date, "%b %d, %Y - %H:%M:%S")
full_name_month = datetime.datetime.strftime(python_date, "%B")
print(full_name_month)
python_new = datetime.datetime.strftime(python_date, "%d.%m.%Y, %H:%M")
print(python_new)
