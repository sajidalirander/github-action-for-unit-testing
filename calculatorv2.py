from pydantic import BaseModel, StrictFloat

class CalculatorInput(BaseModel):
    a: StrictFloat
    b: StrictFloat


def add(a: float, b: float) -> float:
    inputs = CalculatorInput(a=a, b=b)
    return inputs.a + inputs.b

def subtract(a: float, b: float) -> float:
    inputs = CalculatorInput(a=a, b=b)
    return inputs.a - inputs.b

def divide(a: float, b: float) -> float:
    inputs = CalculatorInput(a=a, b=b)
    if inputs.b == 0:
        raise ValueError("Cannot divide by zero.")
    return inputs.a / inputs.b
