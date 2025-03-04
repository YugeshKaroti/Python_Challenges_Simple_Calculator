def is_valid_expression(expression : str) -> bool:
    '''To check whether the expression is valid or not'''
    import re
    if re.match("[\(]?\d+[\s]?[+|\-|*|\/][\s]?\d+[\)]?", expression):
        return True
    else:
        return False