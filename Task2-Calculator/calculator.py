def calculate():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Choose operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operator.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    calculate()