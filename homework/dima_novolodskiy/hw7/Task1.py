numb = 1

while True:
    use_numb = int(input('Введите цифру:'))
    if use_numb == numb:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')