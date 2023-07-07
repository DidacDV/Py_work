def get_input(inp):
    op = inp.split()
    if len(op) != 3:
        raise Exception("Input must have 3 elements (ex: 1.23 + 4)")
    operand1, operation, operand2 = op
    try:
        operand1 = float(operand1)
        operand2 = float(operand2)
    except ValueError:
        print("First and third element must be numbers")
    return operand1, operation, operand2


def calculate(operand1, op, operand2):
  if op == '+':
    return operand1 + operand2
  if op == '-':
    return operand1 - operand2
  if op == '*':
    return operand1 * operand2
  if op == '/':
    return operand1 / operand2
  raise Exception(f"{op} is not a valid operation symbol")

def main():
    print("Enter operation of three elements (ex: 1.23 + 4). Input exit to exit program")
    while True:
        try:
            inp = input()
            if inp == "exit":
                break
            one, two, three = get_input(inp)
            print(calculate(one, two, three))
        except EOFError:
           break



if __name__ == "__main__":
    main()