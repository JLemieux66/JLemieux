#Math functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

#Calculator
def calculate():
    #Variables for the last result and a tuple of all running operations
    last_result = None
    operations = ()

    #If last result is 0
    while True:
        user_input = input("Enter full operation to start, then subsequent operations (+, add, -, sub, *, mult, /, div, clear (clears current value), print (see all operations), reset (resets all operations), exit): ")

        #Exits calculator
        if user_input == "exit":
            break
        #Clears last result value
        elif user_input == "clear":
            last_result = None
        #Resets operations list and clears last result value
        elif user_input == "reset":
            last_result = None
            operations = ()
        #Prints all operations
        elif user_input == "print":
            if operations:
                print(" ".join(operations))
            else:
                print("No operations recorded.")
        #If none of these commands are entered then it is a math operation
        else:
            try:
                #Subsequent operation where last result isn't 0
                #Takes the current value of last result defined by previous operation
                if last_result is not None:
                    #Variable for splitting the user input, separates "+" and "2"
                    parts = user_input.split()
                    #If the length isn't 2 "+ 2" then it must be entered wrong
                    if len(parts) != 2:
                        raise ValueError("Please complete a subsequent operation, i.e + 2")

                    #Operator defined, mathematical operation
                    operator = parts[0]
                    #Operand converts string to decimal number
                    operand = float(parts[1])

                    #All operations and prints value
                    if operator == "+" or operator == "add":
                        last_result = add(last_result, operand)
                        print(last_result)
                    elif operator == "-" or operator == "sub":
                        last_result = sub(last_result, operand)
                        print(last_result)
                    elif operator == "*" or operator == "mult":
                        last_result = mult(last_result, operand)
                        print(last_result)
                    elif operator == "/" or operator == "div":
                        last_result = div(last_result, operand)
                        print(last_result)
                    else:
                        print("Invalid operation.")

                    #Adds operation and result to operations list
                    operations += (f"{user_input} = {last_result}",)

                else:
                #First input must be full operation, like 2 + 2. Assumes last result is 0.
                    #Variable for splitting user input into 3 values. "2" "+" "2"
                    parts = user_input.split()
                    #If the length isn't 3, there must be an issue
                    if len(parts) != 3:
                        raise ValueError("Please complete a full operation, i.e 2 + 2")

                    #Converts to decimal number
                    operand1 = float(parts[0])
                    #Operator defined
                    operator = parts[1]
                    #Converts to decimal number
                    operand2 = float(parts[2])

                    #All operations and prints the value
                    if operator == "+" or operator == "add":
                        last_result = add(operand1, operand2)
                        print(last_result)
                    elif operator == "-" or operator == "sub":
                        last_result = sub(operand1, operand2)
                        print(last_result)
                    elif operator == "*" or operator == "mult":
                        last_result = mult(operand1, operand2)
                        print(last_result)
                    elif operator == "/" or operator == "div":
                        last_result = div(operand1, operand2)
                        print(last_result)
                    else:
                        print("Invalid operation.")

                    #Adds operations and result to operations list
                    operations += (f"{user_input} = {last_result}",)

            except ValueError as e:
                print(str(e))
                print("Invalid input")

calculate()
