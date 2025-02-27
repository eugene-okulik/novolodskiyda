# task_1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# task_2
fist_str = 'результат операции: 42'
second_str = 'результат операции: 514'
third_str = 'результат работы программы: 9'

print(int(fist_str[fist_str.index(':') + 2:]) + 10)
print(int(second_str[second_str.index(':') + 2:]) + 10)
print(int(third_str[third_str.index(':') + 2:]) + 10)

# task_3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
text = 'Students'
text2 = 'study these subjects:'

print(text, ', '.join(students), text2, ', '.join(subjects))


