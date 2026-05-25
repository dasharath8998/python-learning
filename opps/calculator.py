class Calculator:
    # Changed return type to str, and added self
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def multiply(self, a: int, b: int) -> int:
        return a * b

calculator = Calculator()
print(calculator.add(a=10, b=20))
print(calculator.multiply(a=10, b=20))