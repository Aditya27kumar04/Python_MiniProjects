import Calculator_Art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    while True:
        print(Calculator_Art.art)

        num_1 = float(input("What is the first number: "))
        should_accumulate = True

        while should_accumulate:

            for symbol in operations:
                print(symbol)

            operation_symbol = input("Pick an operation: ")
            num_2 = float(input("What is the second number: "))

            calculation_function = operations[operation_symbol]
            answer = calculation_function(num_1, num_2)

            print(f"{num_1} {operation_symbol} {num_2} = {answer}")

            choice = input(
                f"Type 'y' to continue calculating with {answer}, "
                f"or type 'n' to start a new calculation: "
            ).lower()

            if choice == "y":
                num_1 = answer
            else:
                should_accumulate = False
                print("\n" * 20)


calculator()