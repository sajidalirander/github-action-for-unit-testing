def add(a: float, b: float) -> float: # in python int is subtype of float
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be int or float.")
    result = a + b
    if not isinstance(result, (int, float)):
        raise TypeError("Return value must be int or float.")
    return result

def subtract(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be int or float.")
    result = a - b
    if not isinstance(result, (int, float)):
        raise TypeError("Return value must be int or float.")
    return result

def divide(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be int or float.")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    result = a / b
    if not isinstance(result, (int, float)):
        raise TypeError("Return value must be int or float.")
    return result
