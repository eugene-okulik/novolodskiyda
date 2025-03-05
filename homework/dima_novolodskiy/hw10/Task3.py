def operation_ficstur(func):
    def wrapper(*args):
        first, second = args
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        resalt = func(first, second, operation)
        return resalt
    return wrapper


@operation_ficstur
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '*':
        return (first * second)
    elif operation == '/':
        return (first / second)
    elif operation == '-':
        return (first - second)


a, b = map(int, input("Введите два числа через пробел: ").split(' '))

print(f"Результа:{calc(a, b)}")
