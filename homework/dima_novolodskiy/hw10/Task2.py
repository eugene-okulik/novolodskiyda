def repeat_me(func):
    def wrapper(x, count=1):
        resalt = []
        for i in range(count):
            resalt.append(func(x))
        return resalt
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=4)
