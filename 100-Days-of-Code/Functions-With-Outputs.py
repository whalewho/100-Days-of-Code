#Day-10-calculator-start

from art import logo

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
    print(logo)
    num1 = float(input("What's the first number?: "))
    for i in operations:
        print(operations[i])
    continue_cal = True
    
    while continue_cal:
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1,num2)
        
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        next_move = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if next_move == "y":
            num1 = answer
        elif next_move == "n":
            continue_cal = False
            calculator()

calculator()
