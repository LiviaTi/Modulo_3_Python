from typing import Any

def add(num_a:float , num_b:float) -> float:
    result = num_a + num_b
    return (result)

def subtract(num_a:float , num_b:float) -> float:
    result = num_a - num_b
    return (result)

def multiply(num_a:float, num_b:float) -> float:
    result = num_a * num_b
    return (result)

def divide(num_a:float, num_b:float) -> float:
    if (num_b == 0):
        raise ValueError("Cannot divide by zero")
    else:
        result = num_a / num_b
        return (result)

def power(base: int, exponent: int)-> Any:
    result = pow(base,exponent)
    return (result)