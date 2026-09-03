"""Reference implementation for the decorator return-type check."""


def type_check(correct_type):
    """Return a decorator that enforces the decorated function return type."""

    def decorator(function):
        # Wrap the original function so we can inspect its returned value.
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if isinstance(result, correct_type):
                return result
            # Exercise requirement: print marker text and return None on mismatch.
            print("Bad Type")
            return None

        return wrapper

    return decorator
