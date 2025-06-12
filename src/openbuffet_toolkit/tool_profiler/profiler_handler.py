import time
from functools import wraps
from typing import Callable, Optional
from openbuffet_toolkit.tool_logger import LoggerManager


class ProfilerHandler:
    """
    A utility class for profiling function execution time using a decorator.

    This class provides a static method `time_taken` which can be used to decorate
    functions or methods to automatically log their execution duration. The output
    is written to a logger configured via LoggerManager.
    """

    @staticmethod
    def time_taken(label: str = "", precision: int = 4):
        """
        Creates a decorator that logs the execution time of the decorated function.

        This method measures how long a function takes to execute and logs the result
        using the global logger instance obtained from LoggerManager. The output includes
        an optional label and the elapsed time with configurable precision.

        Args:
            label (str): A custom label to prepend to the log message. Default is an empty string.
            precision (int): Number of decimal places to round the execution time. Default is 6.

        Returns:
            Callable: A decorator function that wraps the target function and logs its execution time.
        """
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                logger = LoggerManager().get_logger
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                elapsed = round(end - start, precision)
                message = f"{label}[{func.__name__}] executed in {elapsed} seconds."

                if logger:
                    logger.info(message)
                else:
                    print(message)

                return result
            return wrapper
        return decorator
