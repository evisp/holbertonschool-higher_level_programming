#!/usr/bin/python3
def safe_print_divison(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {:d}".format(div))
    return div
        
