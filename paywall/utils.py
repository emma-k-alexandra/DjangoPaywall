import math

def validate_code(code):
    if not code:
        return False, 'Code must be a 4 digit integer that does not start with 0'

    try:
        code = int(code)

    except ValueError:
        return False, 'Code must be an integer'
    
    if 4 != math.floor(math.log10(code)) + 1: # checking that code is a 4 digit number
        return False, 'Code must be 4 digits long'

    return True, None