def is_even_positive_int(num):
    try: 
        if num >= 0 and num % 2 == 0:
            return True
        else:
            return False
    except TypeError:
        return False

print(is_even_positive_int(123456))
print(is_even_positive_int(-2))
print(is_even_positive_int(123))
print(is_even_positive_int("huffda"))