result = None
operand = None
operator = None
wait_for_number = True

good_operators = "+-*/"
str_instruction = ""

while True:
    if wait_for_number:
        while True:
            operand = input("Enter operand: ")
            try:
                operand = int(operand)
                wait_for_number = False
                try:
                    str_instruction = str(eval(f"{str_instruction}{operand}"))
                    break
                except ZeroDivisionError:
                    print("Division by zero. Enter a non-zero number")
                    continue
            except ValueError:
                print(f"{operand} is not a number. Try again.")
    else:
        while True:
            operator = input("Enter operator: ")
            if operator in good_operators:
                wait_for_number = True
                str_instruction += operator
                break
            elif operator == "=":
                result = float(eval(str_instruction))
                break
            else:
                print(f"{operator} is not '+' or '-' or '*' or '/'. Try again.")

    if result:
        break

print(result)
