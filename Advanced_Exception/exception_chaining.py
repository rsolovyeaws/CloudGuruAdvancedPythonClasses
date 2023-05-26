from traceback import format_stack, format_tb

def my_func():
    raise IOError

def implicit_chaining():
    try:
        my_func()
    except IOError as err:
        1 / 0

def explicit_chaining():
    try:
        my_func()
    except IOError as err:
        raise ValueError("unexpected value") from err

def explicit_nested():
    try:
        explicit_chaining()
    except ValueError as err:
        tb = format_tb(err.__traceback__)
        stacktrace = format_stack()
        
        with open("traceback.txt", "w") as f:
            f.write("\n".join(tb))
        
        with open("stacktrace.txt", "w") as f:
            f.write("\n".join(stacktrace))
        
        print("ValueError caught")
        
explicit_nested()