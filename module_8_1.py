def add_everything_up(a, b):
    try:
        result = a + b
        if isinstance(result, float):
            return round(result, 3)
        else:
            return result
    except TypeError:
        a = str(a)
        b = str(b)
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
