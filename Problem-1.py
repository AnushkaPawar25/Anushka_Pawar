# Problem-1: Create a small calculator which performs operations such as 
# Addition,Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    def calculate(self, a: float, b: float, operation: str) -> float:
        if (operation == "add"):
            return a + b
        elif (operation == "subtract"):
            return a - b
        elif (operation == "multiply"):
            return a * b
        elif (operation == "divide"):
            if (b == 0):
                return "UNDEFINE"
            return a / b
        else:
            return "UNDEFINE OPERATION"


if __name__ == "__main__":
    calc = Calculator()
    a = 5.9
    b = 0
    operation = "divide"
    result = calc.calculate(a, b, operation)
    print(f"Result: {result}")