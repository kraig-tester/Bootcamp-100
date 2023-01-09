from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(first_num, second_num, operation):        
    try:
       result = operations[operation](first_num, second_num)
    except:
       result = None 
       
    return result

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)

running = True

def calculator():
    second_operation = True

    first_num = float(input("What's the first number?: "))

    while second_operation:
        operation = input('+\n-\n*\n/\nPick an operation: ')
        second_num = float(input("What's the next number?: "))
        result = calculate(first_num, second_num, operation)

        if result == None:
            print("Invalid operation. Try again.")
            continue
        else:
            print(f"\n{first_num} {operation} {second_num} = {result}\n")
            
            answer_given = False
            while not answer_given:
                new_operation = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, type 'exit' to quit the program: ").lower()
                answer_given = True

                if new_operation == "y":
                    first_num = result
                elif new_operation == "n":
                    second_operation = False
                    calculator()
                elif new_operation == "exit":
                    second_operation = False
                else:
                    print("Unknown input. Try again")
                    answer_given = False

calculator()
        
