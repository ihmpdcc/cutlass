from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'

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

def enforce_past_date(func):
    def wrapper(self, date):
        try:
            parsed = datetime.strptime(date, DATE_FORMAT)
        except ValueError:
            raise ValueError("Invalid date. Must be in YYYY-MM-DD format.")

        now = datetime.now()
        if parsed > now:
            raise ValueError("Date must be in the past, not the future.")

        func(self, date)

    return wrapper
