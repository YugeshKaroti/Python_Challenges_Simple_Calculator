def calculate(expression : str) -> float:
    '''To calcuate the value'''
    import re, logging
    from datetime import datetime
    if re.match("[\(]?\d+[\s]?[+|\-|*|\/][\s]?\d+[\)]?", expression):
        try:
            result = eval(expression)
            return float(result)
        except Exception as msg:
            logging.error(f"Error calculating '{expression}': {str(msg).capitalize()} is not allowed.")
            print(f"Error: {str(msg).capitalize()} is not allowed.")
    