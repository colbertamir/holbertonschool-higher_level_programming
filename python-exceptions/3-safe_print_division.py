#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    except Exception as e:
        div = None
        print("Exception:", e)
    finally:
        print("Inside result: {}".format(div))
        return div


if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
