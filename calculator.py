class Calculator:
    def __init__(self):
        pass
    
    # Method to add two numbers
    def add(self, a, b):
        return a + b
    
    # Simulated method overloading: add method with default argument
    def add(self, *args):
        return sum(args)
    
    # Method to subtract two numbers
    def subtract(self, a, b):
        return a - b
    
    # Method to multiply two numbers
    def multiply(self, a, b):
        return a * b
    
    # Method to divide two numbers
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    
    # Method to perform all operations
    def perform_operations(self, x, y):
        print(f"Adding {x} and {y}: {self.add(x, y)}")
        print(f"Subtracting {y} from {x}: {self.subtract(x, y)}")
        print(f"Multiplying {x} and {y}: {self.multiply(x, y)}")
        print(f"Dividing {x} by {y}: {self.divide(x, y)}")

# Example usage
if __name__ == "__main__":
    calc = Calculator()
    
    # Perform operations with two numbers
    calc.perform_operations(10, 5)
    
    # Simulated method overloading
    print(f"Sum of multiple numbers (3, 4, 5): {calc.add(3, 4, 5)}")
    print(f"Sum of multiple numbers (1, 2, 3, 4, 5, 6): {calc.add(1, 2, 3, 4, 5, 6)}")
