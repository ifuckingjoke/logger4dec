from functools import wraps

class Logger:
    def __init__(self, *, foreground=0, style=0, background=0):
        self.foreground = foreground
        self.style = style
        self.background = background

    def log(self, text):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print(
                    f"\033[{self.style};{self.foreground};{self.background}m"
                    f"{text}\033[0m"
                )
                return func(*args, **kwargs)
            return wrapper
        return decorator