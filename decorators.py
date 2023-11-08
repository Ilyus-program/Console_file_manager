def add_separators(func):
    def inner(*args, **kwargs):
        print('<' + ('-' * 50) + '>')
        result = func(*args, **kwargs)
        print('<' + ('-' * 50) + '>')
        return result
    return inner
