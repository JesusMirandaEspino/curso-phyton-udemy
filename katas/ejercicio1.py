def make_negative(number):
    if number < 0:
        return number
    return -number


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))
    

def string_to_array(s):
    return s.split(' ')


def close_compare(a, b, margin = 0):
    if margin >= abs(a - b):
        return 0
    
    return -1 if a < b else 1

