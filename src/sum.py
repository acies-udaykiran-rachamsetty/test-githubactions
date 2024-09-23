def division(a, b):
    if b != 0:
        return a // b
    else:
        raise exception("")


def exception(message):
    raise ZeroDivisionError(message)
