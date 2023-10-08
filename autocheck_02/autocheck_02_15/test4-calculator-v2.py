result = None
operand = None
operator = None
wait_for_number = True

good_operators = "+-*/"

while True:
    user_input = input("Enter operand/operator: ")
    if wait_for_number:
        try:
            operand = int(user_input)
            wait_for_number = False
        except ValueError:
            print(f"{user_input} is not a number. Try again.")
            continue
        if not result:
            result = float(operand)
        else:
            try:
                result = float(eval(f"{result} {operator} {operand}"))
            except ZeroDivisionError:
                print("Division by zero. Enter a non-zero number")
                wait_for_number = True
                continue
    else:
        operator = user_input
        if operator in good_operators:
            wait_for_number = True
        elif operator == "=":
            break
        else:
            print(f"{user_input} is not '+' or '-' or '*' or '/'. Try again.")
            continue

if result:
    print(result)
