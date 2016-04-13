
def enforce_dict(func):
    def wrapper(self, arg):
        if type(arg) is not dict:
            raise ValueError("Invalid type provided. Must be a dict.")
        func(self, arg)

    return wrapper

def enforce_int(func):
    def wrapper(self, arg):
        if type(arg) is not int:
            raise ValueError("Invalid type provided. Must be an int.")
        func(self, arg)

    return wrapper

def enforce_string(func):
    def wrapper(self, arg):
        if type(arg) is not str:
            raise ValueError("Invalid type provided. Must be a string.")
        func(self, arg)

    return wrapper
