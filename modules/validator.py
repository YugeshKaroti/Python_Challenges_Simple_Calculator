def is_valid_expression(expression : str) -> bool:
    '''To check whether the expression is valid or not'''
    import re
    if re.match("(\(?\d+[+|\-|*|\/].+\)?)|\(?\d\s?[+|\-|*|\/].+", expression):
        return True
    else:
        return False
