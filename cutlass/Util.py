from datetime import datetime

import os
import sys
import inspect

DATE_FORMAT = '%Y-%m-%d'
PYTHON_MIN_VERSION = (2, 7, 0)
PYTHON_MAX_VERSION = (3, 0, 0)

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

def check_python_version(min_version=PYTHON_MIN_VERSION,
                         max_version=PYTHON_MAX_VERSION,
                         raise_exception_on_fail=False,
                         name=None, print_on_fail=True,
                         exit_on_fail=True,
                         return_error_msg=False):
    """
    Check the Python version compatibility.
    By default this method uses constants to define the minimum and maximum
    Python versions required. It's possible to override this by passing new
    values on ``min_version`` and ``max_version`` parameters.
    It will run a ``sys.exit`` or raise a ``UtilError`` if the version of
    Python detected it not compatible.
    min_version[in]               Tuple with the minimum Python version
                                  required (inclusive).
    max_version[in]               Tuple with the maximum Python version
                                  required (exclusive).
    raise_exception_on_fail[in]   Boolean, it will raise a ``UtilError`` if
                                  True and Python detected is not compatible.
    name[in]                      String for a custom name, if not provided
                                  will get the module name from where this
                                  function was called.
    print_on_fail[in]             If True, print error else do not print
                                  error on failure.
    exit_on_fail[in]              If True, issue exit() else do not exit()
                                  on failure.
    return_error_msg[in]          If True, and is not compatible
                                  returns (result, error_msg) tuple.
    """

    # Only use the fields: major, minor and micro
    sys_version = sys.version_info[:3]

    # Test min version compatibility
    is_compat = min_version <= sys_version

    # Test max version compatibility if it's defined
    if is_compat and max_version:
        is_compat = sys_version < max_version

    if not is_compat:
        if not name:
            # Get the utility name by finding the module
            # name from where this function was called
            frm = inspect.stack()[1]
            mod = inspect.getmodule(frm[0])
            mod_name = os.path.splitext(
                os.path.basename(mod.__file__))[0]
            name = '%s utility' % mod_name

        # Build the error message
        if max_version:
            max_version_error_msg = 'or higher and lower than %s' % \
                '.'.join([str(el) for el in max_version])
        else:
            max_version_error_msg = 'or higher'

        error_msg = (
            '%(name)s requires Python version %(min_version)s '
            '%(max_version_error_msg)s. The version of Python detected was '
            '%(sys_version)s. You may need to install or redirect the '
            'execution of this utility to an environment that includes a '
            'compatible Python version.'
        ) % {
            'name': name,
            'sys_version': '.'.join([str(el) for el in sys_version]),
            'min_version': '.'.join([str(el) for el in min_version]),
            'max_version_error_msg': max_version_error_msg
        }

        if raise_exception_on_fail:
            raise UtilError(error_msg)

        if print_on_fail:
            print('ERROR: %s' % error_msg)

        if exit_on_fail:
            sys.exit(1)

        if return_error_msg:
            return is_compat, error_msg

    return is_compat
