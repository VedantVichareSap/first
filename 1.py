def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculator():
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    print("Logic Calculator")
    print("Operators: +  -  *  /  | quit to exit")

    while True:
        expr = input("\nEnter expression (e.g. 3 + 5): ").strip()
        if expr.lower() == 'quit':
            break

        parts = expr.split()
        if len(parts) != 3:
            print("Invalid format. Use: <number> <operator> <number>")
            continue

        num1_str, op, num2_str = parts
        if op not in operations:
            print(f"Unknown operator '{op}'. Use one of: {', '.join(operations)}")
            continue

        try:
            num1, num2 = float(num1_str), float(num2_str)
            result = operations[op](num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
