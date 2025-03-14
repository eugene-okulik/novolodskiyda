import os
import datetime

base_path = os.path.dirname(__file__)
new_file_path = os.path.join(os.path.dirname(os.path.dirname(base_path)), 'eugene_okulik', 'hw_13', 'data.txt')

def txt_date(path):
    list_date = []
    with open(path) as new_file:
        list_txt = new_file.read().split("\n")
        for i in list_txt:
            str = f"{i[3:i.index(' - ')]}"
            date = datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S.%f")
            list_date.append(date)
    return list_date




base_path = os.path.dirname(__file__)
new_file_path = os.path.join(os.path.dirname(os.path.dirname(base_path)), 'eugene_okulik', 'hw_13', 'data.txt')
list_date = txt_date(new_file_path)

first_date = list_date[0]
new_date = first_date + datetime.timedelta(weeks=1)
print(new_date)


second_date = list_date[1]
day_of_week = second_date.strftime('%A')
print(day_of_week)

third_date = list_date[2]
current_date = datetime.datetime.now()
days_difference = (current_date - third_date).days
print(days_difference)
