from src.customexception import RandomException


def division(a, b):
    if b != 0:
        return a // b
    else:
        raise RandomException(f"{__name__}","b should not be zero")
