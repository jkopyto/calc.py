import sys


def sum_numbers(num1, num2):
    return num1 + num2


def sub_numbers(num1, num2):
    return num1 - num2


def mul_numbers(num1, num2):
    return num1 * num2


def div_numbers(num1, num2):
    if num2 == 0:
        return print("Very funny :))))))")
    else:
        return num1 / num2


switcher = {
    "sum": sum_numbers,
    "sub": sub_numbers,
    "mul": mul_numbers,
    "div": div_numbers
}


def is_digit(s):
    try:
        to_check = s.replace('.', '', 1)
        if to_check[0] == "-":
            return to_check.replace('-', '', 1).isdigit()
        else:
            return to_check.isdigit()
    except:
        return False


def parse_number(num):
    try:
        return int(num)
    except ValueError:
        return float(num)


def get_number_from_user(msg):
    number = input(msg)
    if is_digit(number):
        return parse_number(number)
    else:
        return get_number_from_user(msg)


def get_operation(msg):
    z = input(msg)
    if z.lower() in switcher.keys():
        return z
    else:
        print("There is no operation like that. Type sum/sub/mul/div")
        return get_operation(msg)


def get_variables():

    a = parse_number(sys.argv[1]) if len(sys.argv) >= 2 and is_digit(sys.argv[1]) else get_number_from_user("Please provide first number: ")
    b = parse_number(sys.argv[2]) if len(sys.argv) >= 3 and is_digit(sys.argv[2]) else get_number_from_user("Please provide first number: ")
    op = sys.argv[3] if len(sys.argv) >= 4 and sys.argv[3].lower() in switcher.keys() else get_operation("Please provide valid operation: ")

    return a, b, op


def switch(op, num1, num2):
    func = switcher.get(op)
    return func(num1, num2)


if __name__ == "__main__":
    a, b, operation = get_variables()
    print("Provided data: ", a, b, operation)
    print(switch(operation, a, b))
else:
    print("Calc.py is not main")
