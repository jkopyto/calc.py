import sys


def sum_numbers(num1, num2):
    return num1 + num2


def sub_numbers(num1, num2):
    return num1 - num2


def mul_numbers(num1, num2):
    return num1 * num2


def div_numbers(num1, num2):
    if num2 == 0:
        return print("Bardzo śmieszne :))))))")
    else:
        return num1 / num2


available_operations = {
    "sum": sum_numbers,
    "sub": sub_numbers,
    "mul": mul_numbers,
    "div": div_numbers
}


def get_number_from_user(msg):
    number = input(msg)
    if number.isdigit():
        return int(number)
    else:
        return get_number_from_user(msg)


def get_operation(msg):
    op = input(msg)
    if op.lower() in available_operations.keys():
        return op
    else:
        print("Przeginasz. NIE MA TAKIEJ OPERACJI. Podaj sum/sub/mul/div")
        return get_operation(msg)


def get_variables():
    try:
        a, b, op = sys.argv[1:]
    except:
        a = get_number_from_user("num1: ")
        b = get_number_from_user("num 2: ")
        op = get_operation("op: ")
    return a, b, op


def make_calc(num1, num2, op):
    return available_operations[op](int(num1), int(num2))


if __name__ == "__main__":
    num1, num2, op = get_variables()
    print("Provided data: ", num1, num2, op)
    print(make_calc(num1, num2, op))
