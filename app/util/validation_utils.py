def is_int_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_str_in_length(s, a, b):
    return a <= len(s) <= b
