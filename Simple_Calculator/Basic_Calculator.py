import Calculator_Art

def add(n1,n2):
    return n1+n2


def subtract(n1,n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2


def divide(n1,n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(Calculator_Art.art)
    should_accumulate = True
    num_1 = float(input("What is the first number: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an Operation: ")
        num_2 = float(input("What is the second number: "))
        answer = operations[operation_symbol](num_1, num_2)
        print(f" {num_1}  {operation_symbol}  {num_2} = {answer}")

        choice = input(f"Tyep 'y' to continue calculating with {answer}, or type 'n' to start new calculations : ")

        if choice == "y":
            num_1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()