import sys

global available_operations
available_operations = ["sum", "sub", "mul", "div"]


def check_if_digit(s):
    to_check = s.replace('.', '', 1)
    if to_check[0] == "-":
        return to_check.replace('-', '', 1).isdigit()
    else:
        return to_check.isdigit()


def get_number(num):
    try:
        return int(num)
    except ValueError:
        return float(num)


def get_number_from_user(msg):
    number = input(msg)
    if check_if_digit(number):
        return get_number(number)
    else:
        return get_number_from_user(msg)


def get_operation(msg):
    z = input(msg)
    if z.lower() in available_operations:
        return z
    else:
        print("Przeginasz. NIE MA TAKIEJ OPERACJI. Podaj sum/sub/mul/div")
        return get_operation(msg)


def get_variables():
    a = get_number(sys.argv[1]) if len(sys.argv) >= 2 and check_if_digit(sys.argv[1]) else get_number_from_user(
        "Please provide babo first number i mnie nie trolluj: ")
    b = get_number(sys.argv[2]) if len(sys.argv) >= 3 and check_if_digit(sys.argv[2]) else get_number_from_user(
        "Please provide babo second number i daruj sobie: ")
    operation = sys.argv[3] if len(sys.argv) >= 4 and sys.argv[3].lower() in available_operations else get_operation(
        "Podaj mi co mam z tymi liczbami zrobić: ")
    return [a, b, operation]


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


def switch(num1, num2, op):
    switcher = {
        "sum": sum_numbers,
        "sub": sub_numbers,
        "mul": mul_numbers,
        "div": div_numbers
    }

    func = switcher.get(op)
    print("Result: ", func(num1, num2))


def check_if_main():
    if __name__ == "__main__":
        values = get_variables()
        print("Provided data: ", values[0], values[1], values[2])
        switch(values[0], values[1], values[2])
    else:
        print("Calc.py is not main")


check_if_main()
