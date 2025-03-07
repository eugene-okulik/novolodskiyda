def finish_me(func):
    def wrapper(*args):
        resalt = func(*args)
        print('finished')
        return resalt

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
