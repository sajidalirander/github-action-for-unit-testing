from pydantic import BaseModel, field_validator, StrictFloat

class CalculatorInput(BaseModel):
    a: StrictFloat
    b: StrictFloat

    @field_validator('a', 'b')
    @classmethod
    def must_be_number(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Inputs must be int or float.")
        return value

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
