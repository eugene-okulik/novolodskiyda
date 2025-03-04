from random import randrange, choice


salary = 0
while salary < 10000:
    salary = int(input("Ввидите salary до 10000$: "))
    bonus = choice([True, False])
    if bonus:
        sum_bonus = salary * randrange(1, 31) * 0.01
        salary_with_bonus = salary + sum_bonus
        print(f"{salary}, {bonus} - '${int(salary_with_bonus)}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")
print('Мы столько не платим!!!')
